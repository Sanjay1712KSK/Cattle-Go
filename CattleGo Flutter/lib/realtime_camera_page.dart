import 'dart:convert';

import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:image/image.dart' as img;

import 'app_endpoints.dart';

class RealtimeCameraPage extends StatefulWidget {
  const RealtimeCameraPage({super.key});

  @override
  _RealtimeCameraPageState createState() => _RealtimeCameraPageState();
}

class _RealtimeCameraPageState extends State<RealtimeCameraPage> {
  CameraController? _controller;
  List<CameraDescription>? _cameras;
  bool _isCameraInitialized = false;
  bool _isProcessing = false;
  DateTime? _lastProcessedAt;

  // Store full prediction data
  Map<String, dynamic>? _predictionData;

  final Uri _realtimeApiUri = AppEndpoints.hfSpaceUri('/predict-frame');

  @override
  void initState() {
    super.initState();
    _initializeCamera();
  }

  Future<void> _initializeCamera() async {
    _cameras = await availableCameras();
    if (_cameras != null && _cameras!.isNotEmpty) {
      final CameraDescription selectedCamera = _cameras!.firstWhere(
        (camera) => camera.lensDirection == CameraLensDirection.back,
        orElse: () => _cameras!.first,
      );

      _controller = CameraController(
        selectedCamera,
        ResolutionPreset.medium,
        enableAudio: false,
      );
      await _controller!.initialize();
      if (!mounted) return;

      setState(() {
        _isCameraInitialized = true;
      });

      _controller!.startImageStream((CameraImage image) {
        final DateTime now = DateTime.now();
        final bool shouldThrottle = _lastProcessedAt != null &&
            now.difference(_lastProcessedAt!) < const Duration(milliseconds: 900);

        if (!_isProcessing && !shouldThrottle) {
          _isProcessing = true;
          _lastProcessedAt = now;
          _processCameraImage(image);
        }
      });
    }
  }

  img.Image _convertCameraImage(CameraImage image) {
    final int width = image.width;
    final int height = image.height;
    final int uvRowStride = image.planes[1].bytesPerRow;
    final int uvPixelStride = image.planes[1].bytesPerPixel!;

    final yPlane = image.planes[0].bytes;
    final uPlane = image.planes[1].bytes;
    final vPlane = image.planes[2].bytes;

    final img.Image imageConverted = img.Image(width: width, height: height);

    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        final int uvIndex =
            uvPixelStride * (x / 2).floor() + uvRowStride * (y / 2).floor();
        final int index = y * width + x;

        final int yp = yPlane[index];
        final int up = uPlane[uvIndex];
        final int vp = vPlane[uvIndex];

        final int r = (yp + 1.402 * (vp - 128)).round().clamp(0, 255);
        final int g = (yp - 0.344136 * (up - 128) - 0.714136 * (vp - 128))
            .round()
            .clamp(0, 255);
        final int b = (yp + 1.772 * (up - 128)).round().clamp(0, 255);

        imageConverted.setPixelRgba(x, y, r, g, b, 255);
      }
    }

    return imageConverted;
  }

  img.Image _prepareImageForUpload(CameraImage image) {
    img.Image processed = _convertCameraImage(image);

    final int rotation = _controller?.description.sensorOrientation ?? 0;
    if (rotation == 90 || rotation == 180 || rotation == 270) {
      processed = img.copyRotate(processed, angle: rotation);
    }

    return img.copyResizeCropSquare(processed, size: 256);
  }

  Map<String, dynamic> _normalizePredictionData(dynamic decodedBody) {
    if (decodedBody is! Map<String, dynamic>) {
      return {'message': 'Unexpected response format'};
    }

    final String? predictedClass =
        decodedBody['class']?.toString() ?? decodedBody['breed']?.toString();
    final num? rawConfidence = decodedBody['confidence'] is num
        ? decodedBody['confidence'] as num
        : num.tryParse(decodedBody['confidence']?.toString() ?? '');
    final double? confidence = rawConfidence?.toDouble();

    String message = decodedBody['message']?.toString() ?? '';
    if (message.isEmpty && predictedClass != null && predictedClass.isNotEmpty) {
      message = predictedClass;
      if (confidence != null) {
        message =
            '$message (${(confidence * 100).clamp(0, 100).toStringAsFixed(1)}%)';
      }
    }

    return {
      ...decodedBody,
      'class': predictedClass,
      'confidence': confidence,
      'message': message.isEmpty ? 'Point at cattle...' : message,
    };
  }

  Future<void> _processCameraImage(CameraImage image) async {
    try {
      final img.Image resized = _prepareImageForUpload(image);

      // Compress for upload
      final List<int> jpegBytes = img.encodeJpg(resized, quality: 75);

      final request = http.MultipartRequest(
        'POST',
        _realtimeApiUri,
      );
      request.headers.addAll(AppEndpoints.hfSpaceHeaders());

      request.files.add(http.MultipartFile.fromBytes(
        'file',
        jpegBytes,
        filename: 'frame.jpg',
      ));

      final response = await request.send().timeout(const Duration(seconds: 10));
      final responseBody = await response.stream.bytesToString();

      if (response.statusCode == 200) {
        final data = _normalizePredictionData(jsonDecode(responseBody));
        if (mounted) {
          setState(() {
            _predictionData = data;
          });
        }
      } else {
        if (mounted) {
          setState(() {
            _predictionData = {
              'message': "Server Error: ${response.statusCode}"
            };
          });
        }
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _predictionData = {'message': 'Connection Error'};
        });
      }
    } finally {
      if (mounted) _isProcessing = false;
    }
  }

  @override
  void dispose() {
    _controller?.stopImageStream();
    _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (!_isCameraInitialized || _controller == null) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    // Optional: compute confidence as percentage for a progress bar
    double confidencePercent = 0.0;
    if (_predictionData != null && _predictionData!['confidence'] != null) {
      final dynamic rawConfidence = _predictionData!['confidence'];
      final double? parsedConfidence = rawConfidence is num
          ? rawConfidence.toDouble()
          : double.tryParse(rawConfidence.toString());
      confidencePercent = (parsedConfidence ?? 0.0).clamp(0.0, 1.0);
    }

    return Scaffold(
      appBar: AppBar(title: const Text('Real-time Analysis')),
      body: Stack(
        fit: StackFit.expand,
        children: [
          CameraPreview(_controller!),
          Positioned(
            bottom: 30,
            left: 20,
            right: 20,
            child: Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.black.withOpacity(0.6),
                borderRadius: BorderRadius.circular(15),
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    _predictionData?['message'] ?? "Point at cattle...",
                    textAlign: TextAlign.center,
                    style: const TextStyle(color: Colors.white, fontSize: 18),
                  ),
                  const SizedBox(height: 6),
                  // Optional: confidence bar
                  LinearProgressIndicator(
                    value: confidencePercent,
                    minHeight: 8,
                    backgroundColor: Colors.grey[700],
                    color: Colors.greenAccent,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

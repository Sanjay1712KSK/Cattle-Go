class AppEndpoints {
  static const String hfSpaceBaseUrl = String.fromEnvironment(
    'HF_SPACE_BASE_URL',
    defaultValue: 'https://sanjay11kumar17s-cattle-go-model.hf.space',
  );

  static const String hfSpaceToken =
      String.fromEnvironment('HF_SPACE_TOKEN', defaultValue: '');

  static Uri hfSpaceUri(String path) => Uri.parse('$hfSpaceBaseUrl$path');

  static Map<String, String> hfSpaceHeaders([
    Map<String, String>? extraHeaders,
  ]) {
    return <String, String>{
      if (hfSpaceToken.isNotEmpty) 'Authorization': 'Bearer $hfSpaceToken',
      ...?extraHeaders,
    };
  }
}

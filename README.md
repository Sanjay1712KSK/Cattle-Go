# 🐄 CattleGo — Intelligent Livestock Breed Identification System

## 📌 Overview

CattleGo is a smart livestock management app that helps farmers and researchers identify Indian cattle breeds using AI-based image recognition. It combines machine learning, real-time detection, multilingual support, and a RAG-based chatbot to make livestock management more accessible and efficient.

## 🚀 Features

### 🧠 Breed Detection (AI Model)
- Custom MobileNetV2 model trained for Indian cattle breed classification
- Supports both real-time detection and photo upload
- Achieves **53% accuracy** on validation dataset

### 📱 Frontend
- Built with Flutter for cross-platform use
- Firebase Authentication for secure user login
- Clean UI with options for live camera, image upload, and breed prediction results

### 🌐 Backend
- Model served through FastAPI
- Hosted locally and made public using ngrok for API access
- Handles image uploads and returns predicted breed with confidence score

### 💬 RAG-based Chatbot
- Hosted on a separate server
- Provides breed-related answers and general livestock guidance
- Context-aware and supports user queries dynamically

### 🈳 Multilingual Support
- App available in English, Tamil, and Hindi for wider accessibility

## 🧩 Tech Stack

| Layer | Technologies Used |
|-------|------------------|
| Frontend | Flutter |
| Backend | FastAPI, Python |
| Machine Learning | TensorFlow / Keras (MobileNetV2) |
| Authentication | Firebase |
| Deployment | ngrok (for FastAPI), separate server for chatbot |
| Database | Firebase Firestore (optional for storing user data) |

## ⚙️ Architecture Workflow

1. **User Login** → Firebase Authentication
2. **Choose Detection Mode** → Upload photo or live camera feed
3. **Image Sent to FastAPI Server** → ngrok exposes localhost API
4. **Model (MobileNetV2)** → Predicts cattle breed and returns response
5. **Result Displayed in App** → Breed name + confidence level
6. **Chatbot Interaction** → Users can ask breed-related queries
7. **Multilingual UI** → English, Tamil, Hindi toggle

## 🧠 Machine Learning Model Details

- **Architecture**: MobileNetV2
- **Training Dataset**: Indian cattle breed images
- **Input Size**: 256×256×3
- **Accuracy**: ~53% (Baseline)
- **Framework**: TensorFlow / Keras
- **Optimization Options**: FP16 / INT8 quantization for deployment

## 📊 Model Training Progress

### Performance Analysis
- **Best Performance**: After_finetune3_and_before_finetune4.png
  - Training and validation accuracy converge at ~90%
  - Minimal overfitting, excellent generalization
  - Loss curves decrease smoothly and plateau at low values

- **Worst Performance**: After_finetune1_and_before_finetune2.png
  - Shows signs of overfitting
  - Large gap between training and validation accuracy
  - Validation loss stagnates while training loss decreases

## 📈 Training Evolution

### Stage 1: Initial Fine-tuning (Finetune1 → Finetune2)
```
# Model Accuracy
- Train Accuracy: Rapid increase to ~0.7
- Validation Accuracy: Plateaus at ~0.5-0.55

Accuracy
0.7 |
0.6 |   ● (Train)
0.5 |   ● (Val)
0.4 |
0.3 |
0  2  4  6  8  10 12 14 16 Epoch

# Model Loss
- Train Loss: Decreases steadily
- Validation Loss: Stagnates and shows overfitting

Loss
2.5 |
2.0 |   ● (Val)
1.5 |   ● (Train)
1.0 |
0  2  4  6  8  10 12 14 16 Epoch
```
**Analysis**: Model begins learning but struggles with generalization, showing clear overfitting patterns.

### Stage 2: Improved Generalization (Finetune2 → Finetune3)
```
# Model Accuracy
- Train Accuracy: ~0.8
- Validation Accuracy: ~0.75-0.8 (closely follows training)

Accuracy
0.8 |   ● (Train)
0.7 |   ● (Val)
0.6 |
0.5 |
0.4 |
0.3 |
0    5    10   15   20   25 Epoch

# Model Loss
- Both losses decrease steadily together

Loss
2.5 |
2.0 |
1.5 |   ● (Train) ● (Val)
1.0 |
0    5    10   15   20   25 Epoch
```
**Analysis**: Significant improvement - overfitting addressed, model shows much better generalization.

### Stage 3: Peak Performance (Finetune3 → Finetune4)
```
# Model Accuracy
- Both curves converge at ~0.9 accuracy

Accuracy
0.9 |   ●●● (Train & Val converge)
0.8 |   ●
0.7 |   ●
0.6 |   ●
0.5 |   ●
0.4 |   ●
0.3 |   ●
0.2 |   ●
0    5    10   15   20   25   30 Epoch

# Model Loss
- Perfect synchronization between training and validation

Loss
3.5 |
3.0 |
2.5 |
2.0 |
1.5 |   ●●● (Train & Val sync)
1.0 |
0    5    10   15   20   25   30 Epoch
```
**Analysis**: **Ideal performance** - Model achieves excellent generalization with minimal overfitting.

### Stage 4: Final Optimization (Finetune4 → Finetune5)
```
# Model Accuracy        # Model Loss
- Train Accuracy        - Train Loss
- Validation Accuracy   - Validation Accuracy

## Accuracy             ## Model Loss
- Epoch                 - Epoch
```
**Status**: Final optimization stage (graphs in progress)
**Expected**: Further refinement of model performance

### Final Confusion Matrix
```
# Confusion Matrix

- 40 |
- 30 |
- 20 |
- 10 |
-    +----------------
     Time    Predicted
```
**Purpose**: Final model evaluation across all breed classes
**Usage**: Visualizes classification performance and identifies breed confusion patterns

## 🔍 Future Enhancements

- Improve model accuracy (>80%) with more balanced datasets
- Add offline detection using TensorFlow Lite
- Integrate GPS-based livestock tracking
- Expand chatbot knowledge base for veterinary queries
- Support for more regional languages
- Real-time health monitoring features
- Breed recommendation system for different climates

## 🛠️ Setup & Installation

### Prerequisites
- Flutter SDK
- Python 3.8+
- TensorFlow
- Firebase account
- ngrok account

### Installation Steps
1. Clone the repository
2. Install Flutter dependencies: `flutter pub get`
3. Set up Python backend: `pip install -r requirements.txt`
4. Configure Firebase authentication
5. Start FastAPI server and expose via ngrok
6. Run the Flutter app: `flutter run`

## 📱 Usage

1. **Login**: Users authenticate via Firebase
2. **Detection Mode Selection**:
   - Live Camera: Real-time breed detection
   - Photo Upload: Detect from existing images
3. **Results**: View predicted breed with confidence score
4. **Chat Assistance**: Ask breed-related questions via chatbot
5. **Language Toggle**: Switch between English, Tamil, or Hindi

## 🤝 Contributing

We welcome contributions to improve CattleGo! Areas of interest:
- Model accuracy improvements
- Additional language support
- UI/UX enhancements
- Documentation updates
- Bug fixes and performance optimizations

---

*Note: This documentation reflects the model training progress up to Finetune4, with Finetune5 representing ongoing optimization efforts.*

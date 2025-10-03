# Cattle Breed Recognition Using MobileNetV2

## Project Overview
This project classifies **41 Indian cattle breeds** using a **MobileNetV2 model fine-tuned on our dataset**. It supports:

- **Image upload** via API  
- **Real-time webcam detection**  
- **Confidence scores** for predictions  

---

## Dataset
- 41 Indian cattle breeds, ~95–100 images per breed  
- **Train/Validation/Test split:** 70% / 15% / 15%  
- **Image preprocessing:** resized to 256×256, normalized  
- **Data augmentation:** rotation, shift, shear, zoom, flip, and MixUp  

---

## MobileNetV2 Fine-Tuned Model
- **Base model:** MobileNetV2 (pre-trained)  
- **Top layers:** Custom dense layers with dropout for 41-class classification  
- **Training:** Adam optimizer, categorical crossentropy, early stopping, ReduceLROnPlateau  
- **Result:** ~51% test accuracy  

> Fine-tuning leverages pre-trained features while adapting to our dataset, providing a strong baseline for cattle breed recognition.

---

## Confidence Score
- Model outputs softmax probabilities for all breeds  
- Highest probability = predicted breed  
- Threshold can be set (e.g., 0.6) for uncertain predictions (“unknown”)  

---
## FastAPI Deployment
1. **Install requirements**:  
   ```bash
   pip install fastapi uvicorn tensorflow numpy
2. **Run API**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
3. **Upload image for prediction (example using curl):**
   ```bash
   curl -X POST "http://localhost:8000/predict" -F "file=@path_to_image.jpg"
4. **API returns JSON:**
   ```bash
   {
    "class": "<Breed_Name>",
    "confidence": <float_value>
    }

---
## Requirements

**Python 3.13**

**TensorFlow 2.20+**

**Keras**

**NumPy**

**OpenCV (for webcam detection)**

**FastAPI & Uvicorn**

---

## 🚧 Under Construction

**Real-time detection script**

**Docker integration**

**Database support**

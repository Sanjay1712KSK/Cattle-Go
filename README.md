# Cattle Breed Recognition Using CNN

## Project Overview
This project focuses on **automatically classifying 41 Indian cattle breeds** using a **MobileNetV2 model fine-tuned on our dataset**. It supports both **image upload** and **real-time webcam detection**, producing a **confidence score** for each prediction.

---

## Dataset
- Collected images of **41 Indian bovine breeds**.
- Each breed has ~95–100 images.
- Dataset is split into:
  - **Train:** 70% of images
  - **Validation:** 15% of images
  - **Test:** 15% of images
- Images are **resized to 256×256** and **normalized** (pixel values scaled between 0 and 1).  
- **Data augmentation and MixUp** are applied on the training set to improve generalization.

---

## MobileNetV2 Fine-Tuned Model
- **Base Model:** Pre-trained MobileNetV2  
- **Input:** 256×256×3 RGB images  
- **Fine-Tuning:**  
  - Added custom dense layers on top for 41-class classification  
  - Dropout applied to prevent overfitting  
  - Trained with **Adam optimizer** and **categorical crossentropy loss**  
- **Training Tricks:**  
  - Data augmentation (rotation, shift, shear, zoom, flip)  
  - MixUp augmentation to reduce overfitting  
  - ReduceLROnPlateau & EarlyStopping callbacks for stable training  
- **Result:** Achieved **~51% test accuracy**  

> This fine-tuned MobileNetV2 leverages pre-trained features while adapting to our specific dataset, providing a good baseline for cattle breed recognition.

---

## Confidence Score
- For each prediction, the model outputs a **softmax probability** per breed.  
- The **highest probability** is the predicted breed.  
- A **threshold** can be set (e.g., 0.6) to label uncertain predictions as “unknown”.  
- Confidence score is displayed for both uploaded images and real-time webcam detection.

---

## Requirements
- Python 3.13  
- TensorFlow 2.20+  
- Keras  
- NumPy  
- OpenCV (for real-time detection)  
- FastAPI & Uvicorn (for API deployment)  

## 🚧 Under Construction
Everything beyond this point is currently under development. Check back soon for:
- Real-time detection script
- Docker integration
- API & database support

## Usage
1. **Prepare dataset** in `train/`, `val/`, `test/` folders per breed.  
2. **Run preprocessing** (resize, normalization, augmentation).  
3. **Fine-tune MobileNetV2** with early stopping and MixUp:  
   ```bash
   python finetune_mobilenetv2_mixup.py

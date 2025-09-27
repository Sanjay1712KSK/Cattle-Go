# Cattle Breed Recognition Using CNN

## Project Overview
This project focuses on **automatically classifying 49 Indian cattle breeds** using a **Convolutional Neural Network (CNN) built from scratch**. It supports both **image upload** and **real-time webcam detection**, producing a **confidence score** for each prediction.

---

## Dataset
- Collected images of **49 Indian bovine breeds**.
- Each breed has ~95–100 images.
- Dataset is split into:
  - **Train:** 70% of images
  - **Validation:** 15% of images
  - **Test:** 15% of images
- Images are **resized to 224×224** and **normalized** (pixel values scaled between 0 and 1).  
- **Data augmentation** is applied on the training set to improve generalization.

---

## CNN Architecture
- **Input:** 224×224×3 RGB images  
- **Convolutional Layers:**  
  - Three blocks with increasing filters: 32 → 64 → 128  
  - Each block has two Conv2D layers → BatchNorm → ReLU → MaxPooling → Dropout(0.25)  
- **Fully Connected Layers:**  
  - Dense 512 → BatchNorm → ReLU → Dropout(0.5)  
  - Dense 256 → BatchNorm → ReLU → Dropout(0.5)  
- **Output Layer:** Dense 49 → Softmax (probability distribution over breeds)  
- **Training:**  
  - Optimizer: Adam  
  - Loss: Categorical Crossentropy  
  - Metrics: Accuracy  
  - Supports **EarlyStopping** to prevent overfitting

> This architecture extracts hierarchical features, prevents overfitting, and provides reliable confidence scores for breed predictions.

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

---

## Usage
1. **Prepare dataset** in `train/`, `val/`, `test/` folders per breed.  
2. **Run preprocessing** (resize, normalization, augmentation).  
3. **Train CNN** with early stopping:  
   ```bash
   python <comingsoon.py>
   ```
## <!UNDER CONSTRUCTION!>

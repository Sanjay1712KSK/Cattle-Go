import numpy as np
from tensorflow.keras.preprocessing import image

# Load a test image
img_path = "/path/to/your/test/image.jpg"
img = image.load_img(img_path, target_size=(128, 128))  # use the same size as training
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0   # normalize

# Predict
pred = model.predict(img_array)
class_idx = np.argmax(pred, axis=1)[0]
confidence = np.max(pred)

print("Predicted class:", class_idx, "with confidence:", confidence)

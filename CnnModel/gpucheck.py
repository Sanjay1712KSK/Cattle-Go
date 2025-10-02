'''import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))'''
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np

# Hyperparameters
IMG_HEIGHT, IMG_WIDTH = 224, 224
NUM_CLASSES = 41
BATCH_SIZE = 16
EPOCHS = 1  # just a quick test

# Create dummy data
x_train = np.random.rand(BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, 3).astype(np.float32)
y_train = tf.keras.utils.to_categorical(np.random.randint(0, NUM_CLASSES, BATCH_SIZE), NUM_CLASSES)

x_val = np.random.rand(BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, 3).astype(np.float32)
y_val = tf.keras.utils.to_categorical(np.random.randint(0, NUM_CLASSES, BATCH_SIZE), NUM_CLASSES)

# Simple CNN model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    MaxPooling2D(2,2),
    
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(NUM_CLASSES, activation='softmax')
])

# Compile
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train on dummy data
history = model.fit(
    x_train, y_train,
    validation_data=(x_val, y_val),
    epochs=EPOCHS
)

# Check if GPU is used
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))



from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# --- Step 1: Load old model ---
model = load_model("cnn_model.h5")
model.summary()

# --- Step 2: Freeze convolutional base ---
for layer in model.layers[:-7]:  # freeze all layers except the old Dense layers
    layer.trainable = False

# --- Step 3: Remove old Dense layers ---
for _ in range(7):
    model.pop()  # remove last layers sequentially

# --- Step 4: Add new smaller top layers ---
model.add(Flatten(name='flatten_new'))
model.add(Dense(256, activation='relu', name='dense256_new'))
model.add(BatchNormalization(name='bn256_new'))
model.add(Dropout(0.5, name='dropout256_new'))
model.add(Dense(128, activation='relu', name='dense128_new'))
model.add(BatchNormalization(name='bn128_new'))
model.add(Dropout(0.5, name='dropout128_new'))
model.add(Dense(41, activation='softmax', name='output_new'))

# --- Step 5: Compile ---
model.compile(
    optimizer=Adam(1e-3),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# --- Step 6: Data generators ---
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    "/home/sanjaykumars/Desktop/Hacktrix/dataset_preprocessed/train",
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical'
)

val_data = val_datagen.flow_from_directory(
    "/home/sanjaykumars/Desktop/Hacktrix/dataset_preprocessed/val",
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical'
)

# --- Step 7: Train top layers only ---
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=20
)

# --- Step 8: Save fine-tuned model ---
model.save("cnn_model_finetuned.h5")
print("Fine-tuned model saved!")

# --- Optional Step 9: Unfreeze some conv layers later ---
for layer in model.layers[-15:]:  # unfreeze last 15 layers for full fine-tuning
    layer.trainable = True
model.compile(optimizer=Adam(1e-4), loss='categorical_crossentropy', metrics=['accuracy'])
history2 = model.fit(train_data, validation_data=val_data, epochs=10)

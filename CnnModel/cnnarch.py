'''from tensorflow import keras
model = keras.models.load_model("cnn_model.h5")
model.summary()'''
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(41, activation='softmax'))
model.add(Flatten())
model.add(Dense(256, activation='relu'))  # smaller
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))  # smaller
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(41, activation='softmax'))

from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_path = "/home/sanjaykumars/Desktop/Hacktrix/dataset_preprocessed/train"
val_path   = "/home/sanjaykumars/Desktop/Hacktrix/dataset_preprocessed/val"
test_path  = "/home/sanjaykumars/Desktop/Hacktrix/dataset_preprocessed/test"
batch_size = 32
img_size = (224, 224)
train_datagen = ImageDataGenerator(
    rescale=1.0,   
    horizontal_flip=True,  
    zoom_range=0.1
)
val_datagen = ImageDataGenerator(rescale=1.0)
test_datagen = ImageDataGenerator(rescale=1.0)
train_generator = train_datagen.flow_from_directory(
    train_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)
val_generator = val_datagen.flow_from_directory(
    val_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)
test_generator = test_datagen.flow_from_directory(
    test_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)
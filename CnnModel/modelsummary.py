from tensorflow.keras.models import load_model

model = load_model("cnn_model_finetuned.h5")

# Save summary to a file
with open("model_description.txt", "w") as f:
    model.summary(print_fn=lambda x: f.write(x + "\n"))

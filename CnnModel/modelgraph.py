'''from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import load_model

# Load your saved model
model = load_model("cnn_model.h5")

# Save model diagram to a file
plot_model(model, to_file="cnn_model.png", show_shapes=True, show_layer_names=True)'''

import tensorflow as tf
import visualkeras
from PIL import ImageFont

# Load your saved model
model = tf.keras.models.load_model("cnn_model.h5")

# Optional: custom font (otherwise it uses default)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = None

# Generate visualization
visualkeras.layered_view(
    model, 
    legend=True, 
    font=font
).show()


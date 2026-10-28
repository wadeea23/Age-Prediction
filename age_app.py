
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("/content/age_model.keras")

st.title("Age Estimator")

uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

open_camera = st.checkbox("Open Camera")

camera_image = None

if open_camera:
    camera_image = st.camera_input("Take a Photo")

if uploaded_image is not None:
    image_file = uploaded_image
elif camera_image is not None:
    image_file = camera_image
else:
    image_file = None

if image_file is not None:
    image = Image.open(image_file)
    st.image(image)

    if st.button("Predict Age"):
        image = image.convert("RGB").resize((48, 48))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        prediction = model.predict(image, verbose=0)
        age = round(prediction[0][0])

        st.success(f"Estimated Age: {age} years old")

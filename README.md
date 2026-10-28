# Age Estimation from Face Images

## 1. Project Overview

This project uses a CNN model to predict a person's age from a face image.

The images are resized to 48 × 48 pixels.

## 2. Setup Steps

1. Open the notebook in Google Colab.
2. Upload the dataset.
3. Load and prepare the images.
4. Train and test the model.
5. Save the model.
6. Run the Streamlit app to predict age from an image.

## 3. Model Architecture

The model uses the following layers:

- **Conv2D:** Finds features in the images.
- **MaxPooling2D:** Reduces image size.
- **Flatten:** Changes the image into a one-dimensional array.
- **Dense:** Learns from the image features.
- **Output Layer:** Predicts the person's age.

## 4. Model Performance

The model was tested using test images.

The model can predict age, but some predictions may be incorrect.

## 5.Limitations

- **Lighting:** Poor lighting may affect the results.
- **Image Quality:** Blurry images may reduce accuracy.
- **Facial Differences:** People of the same age can look different.
- **Age Groups:** The model may make more mistakes for age groups with fewer images.
- **Ethical Considerations:** The predicted age is only an estimate.

## 6. Conclusion

This project shows how a CNN model can predict age from face images. However, the predictions are not always correct and should be treated as estimates.

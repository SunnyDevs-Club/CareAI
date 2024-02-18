from keras.preprocessing import image
import numpy as np
import joblib

from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

mode = joblib.load('ai/mri.pkl')

labels=[
    'No Impairment, You are healthy:)',
    'Very Middle Impairment', 
    'Mild Impairment, double check with doctors', 
    'Moderate Impairment. You should definitely contact with the doctor.'
    ]

def predict_image(file):
    # Load and preprocess the image
    img = image.load_img(convert_uploaded_file_to_bytes_io(file), target_size=(150, 150))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    # Make predictions
    predictions = mode.predict(img)
    
    # Get the predicted class label
    predicted_class = np.argmax(predictions[0])
    
    # Get the corresponding class name
    class_name = labels[predicted_class]
    
    return predicted_class, class_name


def convert_uploaded_file_to_bytes_io(uploaded_file: InMemoryUploadedFile):
    # Read the content of the uploaded file
    file_content = uploaded_file.read()
    # Create a BytesIO object from the content
    bytes_io = BytesIO(file_content)
    # Now you can use bytes_io with functions that require a BytesIO object
    return bytes_io


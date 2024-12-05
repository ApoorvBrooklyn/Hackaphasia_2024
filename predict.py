import tensorflow as tf
import numpy as np

# Load the pretrained model (Update path to your model)
model = tf.keras.models.load_model('learning_type_classifier.h5.h5')

# Define the class labels for your Learning_Type prediction
learning_types = ["Comprehensive Learner", "Auditory Learner", "Visual Learner"]  # Modify this as per your model output

# Preprocessing function (if needed, e.g., normalization or reshaping)
def preprocess_input(data):
    """
    Preprocess the input data to match the format expected by the model.
    This may include reshaping, scaling, etc., based on how the model was trained.
    """
    # Assuming no normalization or scaling was applied in the model training
    # If scaling was used (e.g., using MinMaxScaler or StandardScaler), apply that here
    processed_data = np.array(data).reshape(1, -1)  # Reshaping to match the model's expected input
    return processed_data

# Prediction function
def predict_learning_preference(data):
    # Preprocess the data
    processed_data = preprocess_input(data)
    
    # Make the prediction using the model
    prediction = model.predict(processed_data)
    
    # Assuming the model outputs probabilities for each class
    predicted_class = np.argmax(prediction, axis=1)[0]
    
    # Return the predicted class (Learning Type)
    return learning_types[predicted_class]

from flask import Flask, request, jsonify
from flask_cors import CORS
from Chat import start_chatbot

 # Initialize Flask
app = Flask(__name__)
CORS(app)

@app.route('/quiz1', methods=['POST'])
def predict():
    
    data = request.get_json()
    print(data)
    
    return jsonify({"message": "Hello"})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.get_json()
    if user_input and user_input.get('message'):
        # Assuming `start_chatbot` is a function you created for chatbot functionality
        response = start_chatbot(user_input['message'])
        return jsonify({"message": response})
    else:
        return jsonify({"message": "No input provided!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json
# from predict import predict_learning_preference  # Import the prediction function

# app = Flask(__name__)
# CORS(app)

# @app.route('/quiz1', methods=['POST'])
# def predict():
#     # Extract the data from the frontend request
#     data = request.get_json()
    
#     # Check if the necessary keys are present in the data
#     if data and 'quizData' in data and 'userName' in data and 'userAge' in data:
#         # Extract relevant data from frontend (quiz data and other features)
#         user_age = data['userAge']
#         quiz_data = data['quizData']
        
#         # Prepare the features (e.g., Age, Accuracy and Time values)
#         features = [
#             int(user_age),  # Age (convert to integer)
#             quiz_data['audio']['marks'],  # Accuracy_Audio
#             quiz_data['comprehension']['marks'],  # Accuracy_Comprehension
#             quiz_data['image']['marks'],  # Accuracy_Image
#             quiz_data['audio']['timeTaken'],  # Time_Audio
#             quiz_data['comprehension']['timeTaken'],  # Time_Comprehension
#             quiz_data['image']['timeTaken']  # Time_Image
#         ]
        
#         # Get the predicted learning preference
#         predicted_output = predict_learning_preference(features)
        
#         # Return the prediction as a response
#         return jsonify({"message": f"Predicted Learning Preference: {predicted_output}"})
#     else:
#         return jsonify({"message": "Invalid input provided!"}), 400

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.get_json()
#     if user_input and user_input.get('message'):
#         # Assuming `start_chatbot` is a function you created for chatbot functionality
#         response = start_chatbot(user_input['message'])
#         return jsonify({"message": response})
#     else:
#         return jsonify({"message": "No input provided!"}), 400

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('best_svm_model.pkl')

credit_score = {
    0: "Good",
    1: "Poor",
    2: "Standard"
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    There should be a process of normalizing the actual values. Due to lack of time,
    I did not do it, the app works with normalized values.
    :return:
    """
    features = {feature: float(request.form[feature]) for feature in request.form}
    features_df = pd.DataFrame([features])
    # Predict using the loaded model
    prediction = model.predict(features_df)

    # Return the prediction as JSON
    return jsonify({'Credit Score': credit_score[int(prediction[0])]})


if __name__ == "__main__":
    app.run(debug=True)

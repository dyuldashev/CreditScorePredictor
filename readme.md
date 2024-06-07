# Credit Score Predictor

Welcome to the Credit Score Predictor project! This web application uses a machine learning model to predict credit scores based on various financial inputs.

## Author
- **Name:** Dilshod Yuldoshev
- **Subject:** Machine Learning
- **Topic:** Credit Score Predictor

## Description
This project aims to predict credit scores using a trained Support Vector Machine (SVM) model. Users can input various financial details, and the application will classify their credit score into one of three categories: Good Credit, Average Credit, or Bad Credit.

## Features
- Input various financial details to get a credit score prediction.
- Predicts credit scores using a pre-trained SVM model.
- Provides a user-friendly interface for inputting data and viewing results.

## Required Features
The following features are used to predict the credit score:
- Outstanding Debt
- Interest Rate
- Credit Mix
- Changed Credit Limit
- Delay from Due Date
- Credit History Age
- Number of Credit Inquiries
- Monthly Balance
- Amount Invested Monthly
- Credit Utilization Ratio
- Total EMI per Month
- Number of Delayed Payments
- Number of Credit Cards
- Monthly In-hand Salary
- Annual Income

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/dyuldashev/CreditScorePredictor.git
    cd credit-score-predictor
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python app.py
    ```

5. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

## Usage
1. Open the web application in your browser.
2. Fill in the financial details in the input fields.
3. Click the "Predict" button to get your credit score prediction.

## File Structure
- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the home page where users can input their data.
- `static/styles.css`: The CSS file for styling the web application.
- `best_svm_model.pkl`: The pre-trained SVM model file.


## Contact
For any questions or issues, please contact Dilshod Yuldoshev.

---

Thank you for using the Credit Score Predictor!

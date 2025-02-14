# Diabetes Prediction Model

## Overview
This project is a **Diabetes Prediction Model** that utilizes various classification algorithms for prediction, with the final selection based on **Support Vector Machine (SVM)**. The model has been optimized using **SMOTE** for resampling and **GridSearchCV** for hyperparameter tuning.

## Features
- **Dataset Included**: The project comes with a preprocessed dataset for training and testing.
- **All Models Included**: Multiple classification models are tested for performance.
- **Hyperparameter Tuning**: GridSearchCV is used to find the best parameters.
- **Easy-to-Use UI**: A user-friendly web interface built with Flask.

## Models Tested
The following classification models were tested:
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- XGBoost Classifier
- Support Vector Classifier (SVC) *(Final Selection)*

## Directory Structure
```
DiabetesPrediction/
│── Notebooks/
│   ├── Analysis.ipynb         # Jupyter notebook for data analysis
│
│── Resources/                 # Dataset and trained models
│   ├── diabetes.csv
│   ├── Imputed_final.csv
│   ├── model.pkl              # Trained classification model
│   ├── scaler.pkl             # Scaler for preprocessing
│
│── static/                    # Static files (CSS, images, JS)
│   ├── style.css              # CSS for styling the UI
│
│── templates/                 # HTML templates for Flask app
│   ├── form.html              # Main UI page for input & results
│
│── app.py                     # Flask app entry point
│── README.md                  # Project documentation
│── requirements.txt            # Dependencies list

```

## Installation & Running the Project
Clone the repository and set up the environment:

```bash
git clone https://github.com/mShubham18/DiabetesPrediction.git
cd DiabetesPrediction
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application
Run the Flask application:

```bash
python app.py
```
Then, open your browser and go to:

```
http://127.0.0.1:5000/
```

`Now you can enter the required inputs, and the model will predict whether the person is diabetic or not.`

Feel free to contribute on this project 🙌🏻

Happy Coding ;)


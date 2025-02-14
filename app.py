from flask import Flask,render_template,request
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
with open("Resources/model.pkl","rb") as file:
        model = pickle.load(file)


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main():
    return render_template("form.html")

@app.route("/submit",methods=["POST"])
def submit():
        if request.method=="POST":
            try:
                Pregnancies = float(request.form["Pregnancies"])
                Glucose= float(request.form["Glucose"])
                BloodPressure= float(request.form["BloodPressure"])
                SkinThickness= float(request.form["SkinThickness"])
                Insulin= float(request.form["Insulin"])
                BMI= float(request.form["BMI"])
                DiabetesPedigreeFunction= float(request.form["DiabetesPedigreeFunction"])
                Age= float(request.form["request"])
                input_values = (Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
                input_array = np.asarray(input_values)
                input_array_reshaped = input_array.reshape(1,-1)

                input_data_scaled = scaler.transform(input_array_reshaped)

                predicted_output = model.predict(input_data_scaled)

                return render_template("form.html",prediction = predicted_output)
            except Exception as e:
                 print(f"Unknown Error: {e}")
        

if __name__=="__main__":
    app.run(debug=True)
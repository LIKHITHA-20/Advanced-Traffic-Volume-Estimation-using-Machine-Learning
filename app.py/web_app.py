import numpy as np
import pickle
import joblib
import matplotlib
import matplotlib.pyplot as plt
import time
import pandas
from flask import Flask, request, jsonify, render_template
import os
app=Flask(__name__)
model=pickle.load(open('C:\\Users\\akhil\\OneDrive\\Desktop\\aiml1\\model.pkl', 'rb'))
scale=pickle.load(open('C:\\Users\\akhil\\OneDrive\\Desktop\\aiml1\\label_encoder.pkl','rb'))
@app.route('/')# route to display the home page
def home():
    return render_template('index.html') #rendering the home page
@app.route('/predict', methods=["POST", "GET"])# route to show the predictions in a web UI
def predict():
    #reading the inputs given by the user
    input_feature=[float(x) for x in request.form.values()]
    features_values=[np.array(input_feature)]
    names=[['holiday', 'temp', 'rain', 'snow', 'weather', 'year', 'month', 'day','hours', 'minutes', 'seconds']]
    data=pandas.DataFrame(features_values,columns=names)
    data=scale.fit_transform(data)
    data=pandas.DataFrame(data,columns=names) #predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
    text="Estimated Traffic Volume is:"
    return render_template("index.html", prediction_text=text + str(prediction))
if __name__ == "__main__":  # type: ignore
    app.run(debug=True)

port=int(os.environ.get('PORT', 5000))
app.run(port=port,debug=True,use_reloader=False)

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask (__name__)

#Load pickle model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("Home page.html")

@app.route ("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    if prediction==1:
        return render_template("Home page.html", prediction_text = "there is chance of cancer")
    else:
        return render_template("Home Page.html", prediction_text = "there is no chance of cancer")

if __name__ == "__main__":
    app.run (debug = True)


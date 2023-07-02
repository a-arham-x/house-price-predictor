from flask import Flask, render_template, request
from forms import PredictionForm
from prediction_model import prediction_function
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv

app.config.update(dict(
    SECRET_KEY=os.getenv("SECRET_KEY"),
    WTF_CSRF_SECRET_KEY=os.getenv("WTF_CSRF_SECRET_KEY")
))

@app.route("/")
def hello_world():
    form = PredictionForm()
    return render_template("index.html", predicted_price=0, form=form)

@app.route("/predict", methods=["POST"])
def predict_price():
    form = PredictionForm()
    area = request.form["area"]
    bedrooms = request.form["bedrooms"]
    bathrooms = request.form["bathrooms"]
    stories = request.form["stories"]
    mainroad = request.form["mainroad"]
    guestroom = request.form["guestroom"]
    basement = request.form["basement"]
    hotwaterheating = request.form["hotwaterheating"]
    airconditioning = request.form["airconditioning"]
    parking = request.form["parking"]
    prefarea = request.form["prefarea"]
    furnishingstatus = request.form["furnishingstatus"]
    predicted_price = prediction_function(area, bedrooms, bathrooms, stories, mainroad, guestroom,
         basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus)
    return render_template("index.html", predicted_price=predicted_price, form=form)

if __name__ == "__main__":
    app.run(debug=True)
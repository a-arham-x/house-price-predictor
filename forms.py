from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired

class PredictionForm(FlaskForm):
    area = IntegerField(label="Enter Area", validators=[InputRequired()])
    bedrooms = IntegerField(label="No. of Bedrooms", validators=[InputRequired()])
    bathrooms = IntegerField(label="No. of Bathrooms", validators=[InputRequired()])
    stories = IntegerField(label="No. of Stories", validators=[InputRequired()])
    mainroad = SelectField(label="Mainroad", choices=[(1, "yes"), (0, "no")])
    guestroom = SelectField(label="Guestroom", choices=[(1, "yes"), (0, "no")])
    basement = SelectField(label="Basement", choices=[(1, "yes"), (0, "no")])
    hotwaterheating = SelectField(label="Hot Water Heating", choices=[(1, "yes"), (0, "no")])
    airconditioning = SelectField(label="Air-Conditioning", choices=[(1, "yes"), (0, "no")])
    parking = IntegerField(label="Parking", validators=[InputRequired()])
    prefarea = SelectField(label="Prefarea", choices=[(1, "yes"), (0, "no")])
    furnishingstatus = SelectField(label="Furnishing Status", choices=[(-1, "Unfurnished"), (0, "Semi-Furnished"), [1, "Furnished"]])
    predict = SubmitField(label="Predict")
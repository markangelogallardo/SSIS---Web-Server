from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
import app.models as models

class CollegeForm(FlaskForm):
    college_code= StringField('College Code:', [validators.DataRequired(), validators.Length(max=15, message="Length of Code is past the limit")])
    college_name = StringField('College Name:', [validators.DataRequired(message="No input entered")])
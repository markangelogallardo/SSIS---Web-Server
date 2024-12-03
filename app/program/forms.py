from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
import app.models as models

class ProgramForm(FlaskForm):
    prog_code= StringField('Program Code:', [validators.DataRequired(), validators.Length(max=15, message="Length of Code is past the limit")])
    prog_name = StringField('Program Name:', [validators.DataRequired(message="No input entered")])
    college_code = SelectField('College Code:', [validators.DataRequired()], choices=[("", "")])
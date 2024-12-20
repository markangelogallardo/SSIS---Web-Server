from flask_wtf import FlaskForm
from wtforms import StringField, FileField, validators, SelectField
import app.models as models

class StudentForm(FlaskForm):
    id_num= StringField('ID Number:', [validators.DataRequired(), validators.Length(min=9, max=9, message="ID Number length is invalid"), validators.Regexp(regex="\d{4}-\d{4}",message="ID Number format is invalid")])
    first_name = StringField('First Name:', [validators.DataRequired(message="No input entered")])
    last_name = StringField('Last Name:', [validators.DataRequired(message="No input entered")])
    prog_code = SelectField('Program Code:', [validators.DataRequired()], choices=[("", "")])
    year = SelectField('Year Level:', [validators.DataRequired()], choices=[('1st year'), ('2nd year'), ('3rd year'), ('4th year')])
    gender = SelectField('Gender:', [validators.DataRequired(message="No input entered")], choices=[('Male'), ('Female'), ('Rather not specify')])



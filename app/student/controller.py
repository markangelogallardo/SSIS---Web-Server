from flask import render_template, redirect, request, jsonify
from . import student_bp
import app.models as models
#from app.user.forms import UserForm

@student_bp.route('/student')
@student_bp.route('/')
def index():
    students = models.Students.all()
    return render_template('students/student.html', data=students, title='Home',something='something')
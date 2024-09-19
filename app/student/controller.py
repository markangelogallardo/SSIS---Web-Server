from flask import render_template, redirect, request, jsonify
from . import student_bp
#import app.models as models
#from app.user.forms import UserForm

@student_bp.route('/student')
@student_bp.route('/')
def index():
    return render_template('students/student.html', title='Home',something='something')
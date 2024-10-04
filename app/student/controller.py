from flask import render_template, redirect, request, jsonify
from . import student_bp
import app.models as models
#from app.user.forms import UserForm

@student_bp.route('/student')
@student_bp.route('/')
def index():
    students = models.Students.all()
    return render_template('students/student.html', data=students, title='Home',something='something')

@student_bp.route('/student/add', methods=['POST','GET'])
def register():
    students = models.Students.all()
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(email=form.email.data, password=form.password.data,username=form.username.data)
        user.add()
        return redirect('/')
    else:
        return render_template('students/add_student.html', data=students, title='Home')
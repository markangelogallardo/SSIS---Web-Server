from flask import render_template, redirect, request, jsonify
from . import student_bp
import app.models as models
from app.student.forms import StudentForm

@student_bp.route('/student', methods=['POST','GET'])
@student_bp.route('/', methods=['POST', 'GET'])
def index():
    students = models.Students.all()
    programs = models.Programs.all()
    form = StudentForm(request.form)
    form.prog_code.choices = [(None, "Not Enrolled")] + [(program[0], program[0] + " (" + program[1] +")") for program in programs]
    if request.method == 'POST' and form.validate():
        add_student = models.Students(id_num=form.id_num.data, 
                                f_name=form.first_name.data, 
                                l_name=form.last_name.data, 
                                prog=form.prog_code.data if form.prog_code.data != 'None' else None, 
                                year_lvl=form.year.data, 
                                gender=form.gender.data)
        add_student.add()
        return redirect('/')
    else:
        return render_template('students/student.html', data=students, title='Home', form=form)

'''@student_bp.route('/student', methods=['POST','GET'])
def register():
    students = models.Students.all()
    form = StudentForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(email=form.email.data, password=form.password.data,username=form.username.data)
        user.add()
        return redirect('/')
    else:
    return render_template('students/student.html', title='Home', form=form)'''
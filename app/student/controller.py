from flask import render_template, redirect, request, jsonify, flash, url_for
from . import student_bp
import app.models as models
from app.student.forms import StudentForm
from app import mysql

@student_bp.route('/student', methods=['POST','GET'])
@student_bp.route('/', methods=['POST', 'GET'])
def index():
    students = models.Students.all()
    return render_template('students/student.html', data=students, title='Home')
    
@student_bp.route('/student/add', methods=['POST','GET'])
def add_student():
    form = StudentForm(request.form)
    programs = models.Programs.all()
    id_num = form.id_num.data
    f_name = form.first_name.data
    l_name = form.last_name.data
    prog = form.prog_code.data
    year_lvl = form.year.data
    gender = form.gender.data
    form.prog_code.choices = [(None, "Not Enrolled")] + [(program[0], program[0] + " (" + program[1] +")") for program in programs]
    if request.method == 'POST': 
        if form.validate():
            add_student = models.Students(id_num=id_num, 
                                    f_name=f_name, 
                                    l_name=l_name, 
                                    prog=prog if prog != 'None' else None, 
                                    year_lvl=year_lvl, 
                                    gender=gender)
            try:
                add_student.add()
                #return jsonify(success=True)
                flash(f"Student has been succesfully added!", "success")
            except mysql.connection.Error as e:
                flash(models.Students.input_error(e), "danger")
                #return jsonify({'error': models.Students.input_error(e)})
                
        else:
            flash(f"Student has been succesfully added!", "success")
            #return redirect('/student')
        
    return render_template('students/studentForms.html', title='Add Student', form=form)

@student_bp.route('/student/edit/<student_id>', methods=['POST','GET'])
def edit_student(student_id):
    form = StudentForm(request.form)
    to_be_edited = models.Students.get(student_id)

    return render_template('students/studentForms.html', title='Edit Student', form=form)
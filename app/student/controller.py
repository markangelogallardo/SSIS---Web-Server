from flask import render_template, redirect, request, jsonify, flash, url_for
from . import student_bp
import app.models as models
from app.student.forms import StudentForm
from app import mysql
import numpy as np

@student_bp.route('/student', methods=['POST','GET'])
@student_bp.route('/', methods=['POST', 'GET'])
def student_page():
    students = models.Students.all()
    return render_template('students/student.html', data=students, title='Students')


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
    if request.method == "GET":
        return render_template('students/studentForms.html', title='Add Student', form=form)
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
            except mysql.connection.Error as e:
                flash(models.Students.input_error(e), "danger")

    return render_template('students/studentForms.html', title='Add Student', form=form)

@student_bp.route('/student/edit/<student_id>', methods=['POST','GET'])
def edit_student(student_id):
    form = StudentForm(request.form)
    programs = models.Programs.all()
    form.prog_code.choices = [(None, "Not Enrolled")] + [(program[0], program[0] + " (" + program[1] +")") for program in programs]
    orig_data = models.Students.get(student_id)
    if request.method == "GET":
        form.id_num.data = orig_data[0]
        form.first_name.data = orig_data[1]
        form.last_name.data = orig_data[2]
        form.prog_code.data = orig_data[3]
        form.year.data = orig_data[4]
        form.gender.data = orig_data[5]

        return render_template('students/studentForms.html', title='Edit Student', form=form)
    
    if request.method == "POST":
        edit_student = models.Students(id_num=orig_data[0], 
                                    f_name=form.first_name.data, 
                                    l_name=form.last_name.data, 
                                    prog=form.prog_code.data if form.prog_code.data != 'None' else None, 
                                    year_lvl=form.year.data, 
                                    gender=form.gender.data)
        form_arr = [form.id_num.data, form.first_name.data, form.last_name.data, form.prog_code.data, form.year.data, form.gender.data]    
        orig_arr = np.array(orig_data)
        are_equal = np.array_equal(orig_arr, form_arr)
        try:
            if are_equal:
                flash(f"No changes made", "danger")
            else:
                edit_student.edit()
                flash(f"Edit Succesful!", "success")
        except mysql.connection.Error as e:
                flash(models.Students.input_error(e), "danger")
        
        return render_template('students/studentForms.html', title='Edit Student', form=form)

@student_bp.route('/student/delete/<student_id>', methods=['POST', 'GET'])
def delete_student(student_id):
    if request.method == "GET":
        try:
            models.Students.delete(student_id)
        except:
            flash(f"Unable to delete", "danger")
    return redirect(url_for('student.student_page'))


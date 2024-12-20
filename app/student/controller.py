from flask import render_template, redirect, request, jsonify, flash, url_for
from . import student_bp
import app.models as models
from app.student.forms import StudentForm
from app import mysql
from config import CLOUD_NAME
from cloudinary.utils import cloudinary_url
import numpy as np
import base64
import io
from PIL import Image

@student_bp.route('/student', methods=['POST','GET'])
@student_bp.route('/', methods=['POST', 'GET'])
def student_page():
    students = models.Students.all()
    pictures = {}

    for student in students:
        pictures[student[0]] = models.Students.get_pictures(student[6], student[0]) 

    return render_template('students/student.html', pictures=pictures, data=students, title='Students')


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
    default_prof_pic = f"https://res.cloudinary.com/{CLOUD_NAME}/image/upload/v1734186197/default_pic_hqgvcp.jpg"

    if request.method == "GET":
        return render_template('students/studentForms.html', prof_pic=default_prof_pic, title='Add Student', form=form)
    if request.method == 'POST': 
        if form.validate():
            hasPicture = False
            chosen_prof_pic = request.files['upload-pic']
            #print(request.files)
            if 'upload-pic' in request.files and request.files['upload-pic'].filename != '':
                hasPicture = True
                #prof_pic = Image.open(chosen_prof_pic)
                #buffered = io.BytesIO()
                #prof_pic.save(buffered, format="PNG")
                #prof_pic_val = 'data:image/png;base64,' + base64.b64encode(buffered.getvalue()).decode("utf-8")
            add_student = models.Students(id_num=id_num, 
                                    f_name=f_name, 
                                    l_name=l_name, 
                                    prog=prog if prog != 'None' else None, 
                                    year_lvl=year_lvl, 
                                    gender=gender,
                                    hasPicture=hasPicture)
            try: 
                add_student.add()
                if hasPicture:
                    models.Students.upload_picture(chosen_prof_pic, id_num)
                form = StudentForm(formdata=None)
                hasPicture = False
                flash(f"Added Student! ID Number: " + id_num, "success")
            except mysql.connection.Error as e:
                flash(models.Students.input_error(e), "danger")

    return render_template('students/studentForms.html', prof_pic=default_prof_pic, title='Add Student', form=form)

@student_bp.route('/student/edit/<student_id>', methods=['POST','GET'])
def edit_student(student_id):
    form = StudentForm(request.form)
    programs = models.Programs.all()
    form.prog_code.choices = [(None, "Not Enrolled")] + [(program[0], program[0] + " (" + program[1] +")") for program in programs]
    orig_data = models.Students.get(student_id)
    id_num = orig_data[0]
    prof_pic = models.Students.get_pictures(orig_data[6], orig_data[0]) 
    default_prof_pic = f"https://res.cloudinary.com/{CLOUD_NAME}/image/upload/v1734186197/default_pic_hqgvcp.jpg"
    changePicture = False
    if request.method == "GET":
        id_num = orig_data[0]
        form.first_name.data = orig_data[1]
        form.last_name.data = orig_data[2]
        form.prog_code.data = orig_data[3]
        form.year.data = orig_data[4]
        form.gender.data = orig_data[5]

        return render_template('students/studentForms.html', title='Edit Student', prof_pic=prof_pic, form=form, id_num=id_num)
    
    if request.method == "POST":
        chosen_prof_pic = request.files['upload-pic']
        if 'upload-pic' in request.files and request.files['upload-pic'].filename != '' :
            changePicture = 1
        edit_student = models.Students(id_num=orig_data[0], 
                                    f_name=form.first_name.data, 
                                    l_name=form.last_name.data, 
                                    prog=form.prog_code.data if form.prog_code.data != 'None' else None, 
                                    year_lvl=form.year.data, 
                                    gender=form.gender.data,
                                    hasPicture=changePicture)
        form_arr = [form.first_name.data, form.last_name.data, form.prog_code.data, form.year.data, form.gender.data]    
        orig_arr = np.array(orig_data)
        orig_arr = np.delete(orig_arr, [0,6])
        are_equal = np.array_equal(orig_arr, form_arr)
        print(chosen_prof_pic)
        try:
            if are_equal and changePicture == 0:
                #prof_pic = models.Students.get_pictures(1, orig_data[0]) 
                changePicture = False
                flash(f"No changes made", "danger")
            else:
                if changePicture:
                    models.Students.delete_picture(id_num)
                    models.Students.upload_picture(chosen_prof_pic, id_num)
                else:
                    models.Students.delete_picture(id_num)
                edit_student.edit()
                prof_pic = models.Students.get_pictures(1, orig_data[0]) 
                flash(f"Edit Succesful!", "success")
        except mysql.connection.Error as e:
                flash(models.Students.input_error(e), "danger")
                

        return render_template('students/studentForms.html', title='Edit Student', prof_pic=prof_pic, form=form, id_num=id_num)

@student_bp.route('/student/delete/<student_id>', methods=['POST', 'GET'])
def delete_student(student_id):
    if request.method == "GET":
        try:
            models.Students.delete(student_id)
        except:
            flash(f"Unable to delete", "danger")
    return redirect(url_for('student.student_page'))


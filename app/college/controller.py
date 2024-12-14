from flask import render_template, redirect, request, jsonify, flash, url_for
from . import college_bp
from app.college.forms import CollegeForm
import app.models as models
from app import mysql
import numpy as np

@college_bp.route('/college', methods=['POST','GET'])
def college_page():
    college = models.Colleges.all()
    return render_template('colleges/college.html', data=college, title='Colleges')

@college_bp.route('/college/add', methods=['POST','GET'])
def add_college():
    form = CollegeForm(request.form)
    college_code = form.college_code.data
    college_name = form.college_name.data
    if request.method == "GET":
        return render_template('colleges/collegeForms.html', title='Add College', form=form)
    if request.method == 'POST': 
        if form.validate():
            add_college = models.Colleges(college_code=college_code.upper(), college_name=college_name.upper(), new_college_code=None)
            try:
                add_college.add()
                flash(f"Added College!", "success")
            except mysql.connection.Error as e:
                #flash(e, "danger")
                flash(models.Colleges.input_error(e), "danger")

    return render_template('colleges/collegeForms.html', title='Add College', form=form)

@college_bp.route('/college/edit/<college_code>', methods=['POST','GET'])
def edit_college(college_code):
    form = CollegeForm(request.form)
    orig_data = models.Colleges.get(college_code)
    if request.method == "GET":
        form.college_code.data = orig_data[0]
        form.college_name.data = orig_data[1]

        return render_template('colleges/collegeForms.html', title='Edit College', form=form)
    
    if request.method == "POST":
        edit_college = models.Programs(college_code=orig_data[0],
                                       college_name=form.college_name.data.upper(),
                                        new_prog_code = form.college_code.data)
        form_arr = [form.college_code.data, form.college_name.data]    
        orig_arr = np.array(orig_data)
        are_equal = np.array_equal(orig_arr, form_arr)
        try:
            if are_equal:
                flash(f"No changes made", "danger")
            else:
                edit_college.edit()
                flash(f"Edit Succesful!", "success")
        except mysql.connection.Error as e:
                flash(models.Programs.input_error(e), "danger")
        
        return render_template('colleges/collegeForms.html', title='Edit College', form=form)
    
@college_bp.route('/college/delete/<college_code>', methods=['POST', 'GET'])
def delete_college(college_code):
    if request.method == "GET":
        try:
            models.Colleges.delete(college_code)
        except:
            flash(f"Unable to delete", "danger")
            
    return redirect(url_for('college.college_page'))
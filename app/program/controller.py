from flask import render_template, redirect, request, jsonify, flash, url_for
from . import program_bp
from app.program.forms import ProgramForm
import app.models as models
from app import mysql
import numpy as np

@program_bp.route('/program', methods=['POST','GET'])
def program_page():
    programs = models.Programs.all()
    return render_template('programs/program.html', data=programs, title='Programs')

@program_bp.route('/program/add', methods=['POST','GET'])
def add_program():
    form = ProgramForm(request.form)
    colleges = models.Colleges.all()
    prog_code = form.prog_code.data
    prog_name = form.prog_name.data
    college_code = form.college_code.data
    form.college_code.choices = [(college[0], college[0] + " (" + college[1] +")") for college in colleges]
    if request.method == "GET":
        return render_template('programs/programForms.html', title='Add Program', form=form)
    if request.method == 'POST': 
        if form.validate():
            add_program = models.Programs(prog_code=prog_code.upper(), prog_name=prog_name.upper(), college_code=college_code, new_prog_code=None)
            try:
                add_program.add()
                flash(f"Added Program!", "success")
            except mysql.connection.Error as e:
                #flash(e, "danger")
                flash(models.Programs.input_error(e), "danger")

    return render_template('programs/programForms.html', title='Add Program', form=form)

@program_bp.route('/program/edit/<program_code>', methods=['POST','GET'])
def edit_program(program_code):
    form = ProgramForm(request.form)
    colleges = models.Colleges.all()
    form.college_code.choices = [(college[0], college[0] + " (" + college[1] +")") for college in colleges]
    orig_data = models.Programs.get(program_code)
    if request.method == "GET":
        form.prog_code.data = orig_data[0]
        form.prog_name.data = orig_data[1]
        form.college_code.data = orig_data[2]

        return render_template('programs/programForms.html', title='Edit Program', form=form)
    
    if request.method == "POST":
        edit_program = models.Programs(prog_code=orig_data[0].upper(), 
                                    prog_name=form.prog_name.data.upper(), 
                                    college_code=form.college_code.data, 
                                    new_prog_code = form.prog_code.data.upper())
        form_arr = [form.prog_code.data, form.prog_name.data, form.college_code.data]    
        orig_arr = np.array(orig_data)
        are_equal = np.array_equal(orig_arr, form_arr)
        try:
            if are_equal:
                flash(f"No changes made", "danger")
            else:
                edit_program.edit()
                flash(f"Edit Succesful!", "success")
        except mysql.connection.Error as e:
                flash(models.Programs.input_error(e), "danger")
        
        return render_template('programs/programForms.html', title='Edit Program', form=form)
    
@program_bp.route('/program/delete/<program_code>', methods=['POST', 'GET'])
def delete_program(program_code):
    if request.method == "GET":
        try:
            models.Programs.delete(program_code)
        except:
            flash(f"Unable to delete", "danger")
            
    return redirect(url_for('program.program_page'))
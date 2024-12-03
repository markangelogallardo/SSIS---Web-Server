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
            add_program = models.Programs(prog_code=prog_code, prog_name=prog_name, college_code=college_code)
            try:
                add_program.add()
            except mysql.connection.Error as e:
                #flash(e, "danger")
                flash(models.Programs.input_error(e), "danger")

    return render_template('programs/programForms.html', title='Add Program', form=form)

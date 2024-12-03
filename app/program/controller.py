from flask import render_template, redirect, request, jsonify, flash, url_for
from . import program_bp
import app.models as models
from app import mysql
import numpy as np

@program_bp.route('/program', methods=['POST','GET'])
def program_page():
    programs = models.Programs.all()
    return render_template('programs/program.html', data=programs, title='Programs')

@program_bp.route('/program/add', methods=['POST','GET'])
def add_program():

    return render_template('students/studentForms.html', title='Add Student', form=form)

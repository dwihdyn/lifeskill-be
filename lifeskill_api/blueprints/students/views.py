from flask import Blueprint, jsonify, request
from models.student import Student
from models.teacher import Teacher
# from lifeskill_api.blueprints.students.credAward_faris.main import my_command, my_command2, sofia_response, assistant, after_listen
import speech_recognition as sr
import os
import sys
import re
import requests
import subprocess
from time import strftime
import api.IdentificationServiceHttpClientHelper
import api.IdentifyFile
import api.IdentificationResponse
import api.IdentificationProfile
from dotenv import load_dotenv
import ffmpeg
import pyaudio
import wave
from time import sleep
from lifeskill_api.blueprints.audio.views import voice


# persistent login setup for frontend
from flask_jwt_extended import create_access_token

students_api_blueprint = Blueprint(
    'students_api', __name__, template_folder='templates')


@students_api_blueprint.route('/test', methods=['GET'])
def test():
    resp = {
        'message': 'hi im heree',
        'user': {
            'id': 'user id',
            'username': 'user name',
            'email': 'user email'
        },
        'ok': 'ya'
    }

    return jsonify(resp)


@students_api_blueprint.route('/signup', methods=['POST'])
def signup():
    id_number = request.json['id_number']
    full_name = request.json['full_name']
    password = request.json['password']
    accumulated_score = '100'
    user_group = request.json['user_group']
    # teacher = request.json['teacher_checkbox']

    if Student.get_or_none(id_number=id_number):
        resp = {
            "success": False
        }
        return jsonify(resp)
        # return jsonify(False)

    if Teacher.get_or_none(id_number=id_number):
        resp = {
            "success": False
        }
        return jsonify(resp)

    if user_group == "Student":
        new_user = Student(id_number=id_number, full_name=full_name,
                           password=password, accumulated_score=accumulated_score)

    if user_group == "Teacher":
        new_user = Teacher(id_number=id_number,
                           full_name=full_name, password=password)

    if not new_user.save():
        resp = {
            "success": False
        }
        return jsonify(resp)

    access_token = create_access_token(identity=new_user.id_number)
    resp = {
        "success": True,
        "auth_token": access_token
    }

    return jsonify(resp)


@students_api_blueprint.route('/login', methods=['POST'])
def login():

    id_number = request.json['id_number']
    password = request.json['password']

    student_check = Student.get_or_none(id_number=id_number)
    teacher_check = Teacher.get_or_none(id_number=id_number)

    if student_check is not None:

        if not password == student_check.password:
            response = {
                "success": False
            }
            return jsonify(response)

        else:
            access_token = create_access_token(
                identity=student_check.id_number)
            response = {
                "success": True,
                "authToken": access_token,
                "id": student_check.id,
                "id_number": id_number,
                "full_name": student_check.full_name,
                "isStudent": True


            }
            return jsonify(response)
    else:
        if not password == teacher_check.password:
            response = {
                "success": False
            }
            return jsonify(response)
        else:
            voice()
            access_token = create_access_token(
                identity=teacher_check.id_number)
            response = {
                "success": True,
                "authToken": access_token,
                "id": teacher_check.id,
                "id_number": id_number,
                "full_name": teacher_check.full_name,
                "isStudent": False



            }
            # voice()
            # voice()

            return jsonify(response)


@students_api_blueprint.route('/users/me', methods=['POST'])
def show():
    current_user = request.json['id_number']
    my_account = Student.get_or_none(id_number=current_user)
    if my_account is None:
        my_account = Teacher.get_or_none(id_number=current_user)
        resp = {
            "isStudent": False,
            "id_number": my_account.id_number,
            "full_name": my_account.full_name
        }

        return jsonify(resp)

    resp = {
        "isStudent": True,
        "id_number": my_account.id_number,
        "full_name": my_account.full_name,
        "creativity_score": my_account.creativity_score,
        "leadership_score": my_account.leadership_score,
        "respect_score": my_account.respect_score,
        "accumulated_score": my_account.accumulated_score
    }

    return jsonify(resp)


@students_api_blueprint.route('/scoreboard', methods=['GET'])
def scoreboard():
    query = Student.select().order_by(Student.accumulated_score.desc()).limit(5)
    ranking = []
    for i in query:
        ranking.append({
            "name": i.full_name,
            "score": i.accumulated_score
        })
    print(ranking)
    resp = {
        "ranking": ranking
    }

    return jsonify(resp)


@students_api_blueprint.route('/scoreboard/all', methods=['GET'])
def scoreboard_all():
    query = Student.select()
    ranking = []
    for i in query:
        ranking.append({
            "name": i.full_name,
            "score": i.accumulated_score,
            "anotherScore": i.dropout_score(query)
        })
    # print(ranking)
    sorted_list = sorted(
        ranking, key=lambda k: k['anotherScore'], reverse=True)
    resp = {
        "ranking": sorted_list
    }

    return jsonify(resp)


@students_api_blueprint.route('/getall', methods=['GET'])
def get_all():
    query = Student.select().order_by(Student.full_name)
    students = []
    for i in query:
        students.append(i.full_name)

    resp = {
        "students": students
    }

    return jsonify(resp)


@students_api_blueprint.route('/givepoints', methods=['POST'])
def give_points():
    sel_std = request.json['selStd']
    give_points = request.json['givePoints']
    category = request.json['category']

    student_check = Student.get_or_none(full_name=sel_std)

    if not student_check:
        resp = {
            "success": False
        }

        return jsonify(resp)

    setattr(student_check, category, getattr(
        student_check, category) + int(give_points))
    student_check.save()
    resp = {
        "success": True
    }
    return jsonify(resp)

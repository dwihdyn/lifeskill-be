from lifeskill_web.credAward_faris.main import record_save, my_command, my_command2, sofia_response, assistant, callback
import os
import config
import config
import os
import config
from flask import Blueprint, Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
from models.base_model import db
import peeweedbevolve
import models as m
import speech_recognition as sr
import sys
import re
import requests
import subprocess
from time import strftime, sleep
import api.IdentificationServiceHttpClientHelper
import api.IdentifyFile
import api.IdentificationResponse
import api.IdentificationProfile
import tempfile
import ffmpeg

audio_api_blueprint = Blueprint(
    'audio_api', __name__, template_folder='templates')


source = sr.Microphone()
r = sr.Recognizer()


# @audio_api_blueprint.route('/voice', methods=['POST'])
def voice():

    sofia_response("ready")

    r.listen_in_background(source, callback)

    # assistant(my_command2())


# while True:
    # sleep(999999)


# def start():
#     speaker = api.IdentifyFile.identify_file(
#         sub_key, audio, True, profile)
#     # This functions takes input from microphone and converts input into a string

#     if speaker == profile:
#         assistant(my_command())
#     else:
#         sofia_response("I do not listen to you")
<< << << < HEAD
== == == =


@audio_api_blueprint.route('/upload', methods=['POST'])
def takeAudio():

    print('success')
    # res.setHeader('Access-Control-Allow-Origin', 'http://localhost:5000')
    # breakpoint()
    temp = tempfile.NamedTemporaryFile(suffix='.wav')
    data = request.files['audio'].read()
    temp.write(data)
    temp.seek(0)
    audio_file = temp.name
    file_path = "/".join(audio_file.split("/")[0:-1])
    file_name = audio_file.split("/")[-1]
    subprocess.call(['ffmpeg', '-i', audio_file, '-ar',
                     '16000', (file_path + '/my_' + file_name)])

    # os.write(audio_file, audio)

    # audio, filename = tempfile.mkstemp()

    # breakpoint()
    # os.write(audio, request.files['file'])
    # audio_file = filename + '/' + audio.read()
    # audio = audio.read()
    speaker = api.IdentifyFile.identify_file(
        sub_key, file_path + '/my_' + file_name, True, profile)
    # This functions takes input from microphone and converts input into a string

    if speaker == profile:
        subprocess.call(['ffmpeg', '-i', audio_file, '-ar',
                         '44000', (file_path + '/my2_' + file_name)])
        assistant(my_command(file_path + '/my2_' + file_name))
    else:
        sofia_response("I do not listen to you")

    return print('IM THE BEST')

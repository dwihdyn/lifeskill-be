<<<<<<< HEAD

from lifeskill_web.credAward_faris.main import record_save, my_command, my_command2, sofia_response, assistant, callback
import os
import config
import config
=======
import os
>>>>>>> connecting front to back 50% progress
from flask import Blueprint, Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
<<<<<<< HEAD
from models.base_model import db
import peeweedbevolve
import models as m
import speech_recognition as sr
import sys
import re
import requests
import subprocess
from time import strftime, sleep
=======
>>>>>>> connecting front to back 50% progress


audio_api_blueprint = Blueprint(
    'audio_api', __name__, template_folder='templates')


<<<<<<< HEAD
source = sr.Microphone()
r = sr.Recognizer()


# @audio_api_blueprint.route('/voice', methods=['POST'])
def voice():

    sofia_response("ready")

    r.listen_in_background(source, callback)

    # assistant(my_command2())


# while True:
    # sleep(999999)
=======
ALLOWED_EXTENSIONS = set(['wav'])


@audio_api_blueprint.route('/upload', methods=['POST'])
def takeAudio():
    audio = request.files['file']
    return audio
>>>>>>> connecting front to back 50% progress

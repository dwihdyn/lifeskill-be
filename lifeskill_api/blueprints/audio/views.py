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

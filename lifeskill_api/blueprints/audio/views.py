
from lifeskill_web.credAward_faris.main import record_save, my_command, my_command2, sofia_response, assistant, callback
import os
import config
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
from time import strftime
import api.IdentificationServiceHttpClientHelper
import api.IdentifyFile
import api.IdentificationResponse
import api.IdentificationProfile
import tempfile
import ffmpeg

audio_api_blueprint = Blueprint(
    'audio_api', __name__, template_folder='templates')


sub_key = os.environ.get("KEY1")
profile = os.environ.get("PROFILE_ID")


def my_command(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = my_command()
    return command


# This function convert string into audio


def sofia_response(audio):
    print(audio)
    os.system("say " + audio)


def assistant(command):
    student_list = [sn.fullname.lower() for sn in m.Student.select()]
    points = list(range(5, 51))

    if 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofia_response('Hello Faris. Good morning')
        elif 12 <= day_time < 18:
            sofia_response('Hello Faris. Good afternoon')
        else:
            sofia_response('Hello Faris. Good evening')

    for s in m.Student.select():
        if s.fullname.lower() in command.lower():
            for p in points:
                if str(p) in command:
                    if 'creativity' in command:
                        current_point = s.creativity
                        current_point += p
                        s.creativity = current_point
                        s.save()
                        s.accumulative = s.creativity + s.leadership + s.respect
                        s.save()
                        sofia_response(
                            f"{p} points have been added to {s.fullname}\\'s creativity score")

                    elif 'leadership' in command:
                        current_point = s.leadership
                        current_point += p
                        s.leadership = current_point
                        s.save()
                        s.accumulative = s.creativity + s.leadership + s.respect
                        s.save()
                        sofia_response(
                            f"{p} points have been added to {s.fullname}\\'s leadership score")

                    elif 'respect' in command:
                        current_point = s.respect
                        current_point += p
                        s.respect = current_point
                        s.save()
                        s.accumulative = s.creativity + s.leadership + s.respect
                        s.save()
                        sofia_response(
                            f"{p} points have been added to {s.fullname}\\'s respect score")

                    else:
                        sofia_response("cant hear you")


# def start():
#     speaker = api.IdentifyFile.identify_file(
#         sub_key, audio, True, profile)
#     # This functions takes input from microphone and converts input into a string

#     if speaker == profile:
#         assistant(my_command())
#     else:
#         sofia_response("I do not listen to you")

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
    audio = request.files['file']
    return audio

    print('success')

    audio = request.files['file']
    temp = tempfile.NamedTemporaryFile()
    temp.write(audio.read())
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


@audio_api_blueprint.route('/voice', methods=['POST'])
def voice():

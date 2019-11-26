import models as m
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

load_dotenv()

audio_file = 'voices/voice4andy.wav'
sub_key = os.environ.get("KEY1")
profile = "7ed74eae-db79-4966-907f-c48a494994a9"

# helper = api.IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
#     sub_key)

speaker = apgii.IdentifyFile.identify_file(sub_key, audio_file, True, profile)


# This functions takes input from microphone and converts input into a string


def my_command():
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
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


if speaker == profile:
    assistant(my_command())
else:
    sofia_response("I do not listen to you")

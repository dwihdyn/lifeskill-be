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
<<<<<<< HEAD
import ffmpeg
import pyaudio
import wave
from time import sleep

load_dotenv()


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 16000  # Record at 44100 samples per second
seconds = 6
filename = "output.wav"


def record_save():

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


audio_file = filename
sub_key = '84517f5a452f4a6a8a1a570bab6f40a5'
profile = '201f5139-1049-4dc8-9a99-b7ce0b8e2dd6'
=======

load_dotenv()

audio_file = 'voices/voice4andy.wav'
sub_key = os.environ.get("KEY1")
profile = "7ed74eae-db79-4966-907f-c48a494994a9"
>>>>>>> connecting front to back 50% progress

# helper = api.IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
#     sub_key)

<<<<<<< HEAD
# speaker = api.IdentifyFile.identify_file(sub_key, audio_file, True, profile)


# This functions takes input from microphone and converts input into a strin


def my_command(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        print('Authorizing...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print(audio)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = my_command(audio_file)
    return command


def my_command2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
=======
speaker = api.IdentifyFile.identify_file(sub_key, audio_file, True, profile)


# This functions takes input from microphone and converts input into a string


def my_command():
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
>>>>>>> connecting front to back 50% progress
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
<<<<<<< HEAD

    # with open("microphone-results.wav", "wb") as f:
    #     f.write(audio.get_wav_data())
    #     print(f)

=======
>>>>>>> connecting front to back 50% progress
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
<<<<<<< HEAD
        command = my_command2()
=======
        command = my_command()
>>>>>>> connecting front to back 50% progress
    return command


# This function convert string into audio


def sofia_response(audio):
    print(audio)
    os.system("say " + audio)


def assistant(command):
<<<<<<< HEAD
    student_list = [sn.full_name.lower() for sn in m.Student.select()]
    points = list(range(5, 501))
=======
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
>>>>>>> connecting front to back 50% progress

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


<<<<<<< HEAD
source = sr.Microphone()
r = sr.Recognizer()


def after_listen(recognizer, audio):

    # try:
    speech = recognizer.recognize_google(audio).lower()
    if 'hello' in speech:
        # print("asdf")
        sofia_response("hello")
        sofia_response("how can i help?")
        record_save()
        speaker = api.IdentifyFile.identify_file(
            sub_key, filename, True, profile)
        print(speaker)
        if speaker == profile:
            assistant(my_command(filename))

        else:
            sofia_response("you are not authorized")

    # except sr.UnknownValueError:
    #     print('....')
    #     r.listen_in_background(source, after_listen)


# add 12 points to johns creativity score


r.listen_in_background(source, after_listen)
sleep(9999999)


# record_save()
# speaker = api.IdentifyFile.identify_file(
#     sub_key, filename, True, profile)

# print(filename)

# print(speaker)

# if speaker == profile:
#     sofia_response("you are authorized")
#     assistant(my_command2())

# else:
#     sofia_response("you are not authorized to speak to me")
=======
if speaker == profile:
    assistant(my_command())
else:
    sofia_response("I do not listen to you")
>>>>>>> connecting front to back 50% progress

from time import sleep
import wave
import pyaudio
import ffmpeg
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
sub_key = 'aee065282e114a008db22a19ddc3772e'
profile = ['201f5139-1049-4dc8-9a99-b7ce0b8e2dd6',
           '3839fe26-723e-42d9-93cf-3b0c0f343645']

# helper = api.IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
#     sub_key)

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
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    # with open("microphone-results.wav", "wb") as f:
    #     f.write(audio.get_wav_data())
    #     print(f)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = my_command2()
    return command


# This function convert string into audio


def sofia_response(audio):
    print(audio)
    os.system("say " + audio)


def assistant(command):

    student_list = [sn.full_name.lower() for sn in m.Student.select()]
    points = list(range(5, 501))
    if 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofia_response('Hello Faris. Good morning')
        elif 12 <= day_time < 18:
            sofia_response('Hello Faris. Good afternoon')
        else:
            sofia_response('Hello Faris. Good evening')

    for s in m.Student.select():
        if s.full_name.lower() in command.lower():
            # for p in points:
            #     if str(p) in command:
            p = (re.findall('\d+', command))
            if int(p[0]) <= 50:
                if 'creativity' in command:
                    current_point = s.creativity_score
                    current_point += int(p[0])
                    s.creativity_score = current_point
                    s.save()
                    sofia_response(
                        f"{p} points have been added to {s.full_name}\\'s creativity score")

                elif 'leadership' in command:
                    current_point = s.leadership_score
                    current_point += int(p[0])
                    s.leadership_score = current_point
                    s.save()
                    sofia_response(
                        f"{p} points have been added to {s.full_name}\\'s leadership score")

                elif 'respect' in command:
                    current_point = s.respect_score
                    current_point += int(p[0])
                    s.respect_score = current_point
                    s.save()
                    sofia_response(
                        f"{p} points have been added to {s.full_name}\\'s respect score")

                else:
                    sofia_response("cant hear you")


test = "100 points to alex creativity score"
# print(re.findall('\d+', test))
# assistant(test)


source = sr.Microphone()
r = sr.Recognizer()


def callback(recognizer, audio):
    print("running")

    try:
        speech = recognizer.recognize_google(audio).lower()
        if 'audrey' in speech:
            # print("asdf")
            sofia_response("hello")
            sofia_response("how can i help?")
            record_save()
            speaker = api.IdentifyFile.identify_file(
                sub_key, filename, True, profile)
            print(speaker)
            if speaker in profile:
                assistant(my_command(filename))
            else:
                sofia_response("you are not authorized")
    except sr.UnknownValueError:
        print("re-running")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        # except sr.UnknownValueError:
        #     print('....')
        #     r.listen_in_background(source, after_listen)

        # add 12 points to johns creativity score


r.listen_in_background(source, callback)
# while True:
sleep(999999)


# add 12 points to johns creativity score


# def go():
#     while True:
#         try:
#             r.listen_in_background(source, after_listen)
#             sleep(9999999)

#         except UnknownValueError:
#             go()

# print(filename)

# print(speaker)

# if speaker == profile:
#     sofia_response("you are authorized")
#     assistant(my_command2())

# else:
#     sofia_response("you are not authorized to speak to me")
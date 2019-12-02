import os
import config
from flask import Flask
from models.base_model import db
import peeweedbevolve
import models as m
import speech_recognition as sr
<<<<<<< HEAD
<<<<<<< HEAD
=======
import os
>>>>>>> connecting front to back 50% progress
=======
>>>>>>> front end & back end connectivity established
import sys
import re
import requests
import subprocess
from time import strftime
import api.IdentificationServiceHttpClientHelper
import api.IdentifyFile
import api.IdentificationResponse
import api.IdentificationProfile
<<<<<<< HEAD
<<<<<<< HEAD

=======
from lifeskill_api.blueprints.audio.views import takeAudio
>>>>>>> connecting front to back 50% progress
=======
>>>>>>> front end & back end connectivity established

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'instagram_web')

app = Flask('LIFESKILL', root_path=web_dir)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
<<<<<<< HEAD


@app.cli.command("assistant")
def x():
    from lifeskill_api.blueprints.students.credAward_faris.main import assistant, my_command2
    assistant(my_command2)
=======
>>>>>>> connecting front to back 50% progress

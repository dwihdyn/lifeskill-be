import os
import config
from flask import Flask
from models.base_model import db
import peeweedbevolve
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

from lifeskill_api.blueprints.audio.views import takeAudio

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

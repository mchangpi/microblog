from flask import Flask
from config import MiltonConfig

app = Flask(__name__)

app.config.from_object(MiltonConfig)

from app import routes
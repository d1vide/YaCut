from datetime import datetime

from . import db
from .constants import MAX_LINK_LENGTH


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LINK_LENGTH), nullable=False)
    short = db.Column(db.String(MAX_LINK_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.now)

from datetime import datetime
from random import choice

from flask import url_for

from . import db
from settings import SYMBOLS_LENGTH, USER_INPUT_LIMIT, VALID_SYMBOLS


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'short_link_view', id=self.short, _external=True
            )
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])

    def is_short_link_exists(self, custom_id):
        return bool(self.query.filter_by(short=custom_id).first())

    def get_unique_short_id(self):
        result_short_id = ''
        while len(result_short_id) != SYMBOLS_LENGTH:
            result_short_id += choice(VALID_SYMBOLS)

        if not self.is_short_link_exists(result_short_id):
            return result_short_id
        return self.get_unique_short_id()

    def is_valid_short_link(self, short_link):
        if len(short_link) > USER_INPUT_LIMIT:
            return False
        for value in short_link:
            if value not in VALID_SYMBOLS:
                return False
        return True

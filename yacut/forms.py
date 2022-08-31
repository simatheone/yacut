from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class UrlForm(FlaskForm):
    original = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256)
        ]
    )
    short = ...
    submit = SubmitField('Создать')

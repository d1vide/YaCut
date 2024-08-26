from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, URLField
from wtforms.validators import Optional, DataRequired, Length


class UrlForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), Length(1, 128)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Optional(), Length(1, 16)]
    )
    submit = SubmitField('Создать')

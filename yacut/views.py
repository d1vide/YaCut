from flask import flash, redirect, render_template, url_for

from .forms import UrlForm
from .models import URL_map
from .utils import get_unique_short_id
from . import app, db


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        if URL_map.query.filter_by(original=original_link).first() is not None:
            short_link = url_for('index_view', _external=True) + URL_map.query.filter_by(original=original_link).first().short
        else:
            if custom_id:
                if URL_map.query.filter_by(short=custom_id).first():
                    form.custom_id.errors.append('Такой custom_id уже есть')
                    return render_template('index.html', form=form)
                else:
                    short_link = url_for('index_view', _external=True) + custom_id
                    short_id = custom_id
            else:
                short_id = get_unique_short_id()
                short_link = url_for('index_view', _external=True) + short_id
            obj = URL_map(original=original_link, short=short_id)
            db.session.add(obj)
            db.session.commit()
        flash(f'Ваша ссылка готова: {short_link}', 'free-message')
    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def redirect_view(short_id):
    original_link = URL_map.query.filter_by(short=short_id).first().original
    return redirect(original_link)
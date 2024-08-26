from flask import jsonify, request

from .models import URL_map
from .utils import get_unique_short_id
from . import app, db


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    query_result = URL_map.query.filter_by(short=short_id).first()
    if query_result is None:
        return jsonify({'message':
                        'Указанный id не найден'}), 404
    return jsonify({'url': query_result.original}), 200


@app.route('/api/id/', methods=['POST'])
def create_link():
    if not request.json:
        return jsonify({'message':
                        'Отсутствует тело запроса'}), 400
    original_link = request.json.get('url')
    if not original_link:
        return jsonify({'message':
                        '\"url\" является обязательным полем!'}), 400
    custom_id = request.json.get('short')
    if custom_id is not None:
        if (len(request.json['short']) < 1 or len(request.json['short']) > 16 or URL_map.query.filter_by(short=custom_id).first() is not None):
            return jsonify({'message':
                            'Указано недопустимое имя для короткой ссылки'}), 400
    else:
        custom_id = get_unique_short_id()
    obj = URL_map(original=original_link, short=custom_id)
    db.session.add(obj)
    db.session.commit()
    return jsonify({'url': original_link,
                    'short': custom_id}), 201

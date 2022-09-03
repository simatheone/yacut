from flask import jsonify, request

from . import app, db
from .models import URL_map
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/', methods=('POST',))
def add_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    url_map = URL_map()
    custom_id = data.get('custom_id', None)
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if custom_id is None or not custom_id:
        custom_id = url_map.get_unique_short_id()
        data['custom_id'] = custom_id

    if url_map.is_short_link_exists(data['custom_id']):
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')

    if not url_map.is_valid_short_link(data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_short_url(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first()
    if url_map is not None:
        return jsonify({'url': url_map.original}), 200
    raise InvalidAPIUsage('Указанный id не найден', 404)

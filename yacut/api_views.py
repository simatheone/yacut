from flask import jsonify, request

from . import app, db
from .constants import (ID_NOT_FOUND, INVALID_NAME_FOR_LINK, NAME_IS_OCCUPIED,
                        NO_REQUEST_BODY, REQUIRED_URL)
from .error_handlers import InvalidAPIUsage
from .models import URL_map


@app.route('/api/id/', methods=('POST',))
def add_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(NO_REQUEST_BODY)

    url_map = URL_map()
    custom_id = data.get('custom_id', None)
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_URL)

    if not custom_id or custom_id is None:
        custom_id = url_map.get_unique_short_id()
        data.update({'custom_id': custom_id})

    if url_map.is_short_link_exists(custom_id):
        raise InvalidAPIUsage(
            NAME_IS_OCCUPIED.format(custom_id=custom_id)
        )

    if not url_map.is_valid_short_id(custom_id):
        raise InvalidAPIUsage(INVALID_NAME_FOR_LINK)

    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_short_url(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first()
    if url_map is not None:
        return jsonify({'url': url_map.original}), 200
    raise InvalidAPIUsage(ID_NOT_FOUND, 404)

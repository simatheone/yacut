from flask import flash, redirect, render_template, url_for

from . import app, db
from .constants import INVALID_SYMBOLS, NAME_IS_OCCUPIED_FLASH
from .forms import UrlForm
from .models import URL_map


@app.route('/', methods=('GET', 'POST',))
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        url_map = URL_map()
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = url_map.get_unique_short_id()

        if URL_map.query.filter_by(short=custom_id).first():
            flash(
                NAME_IS_OCCUPIED_FLASH.format(custom_id=custom_id),
                'rejected'
            )
            return render_template('index.html', form=form)

        if not url_map.is_valid_short_id(custom_id):
            flash(
                INVALID_SYMBOLS, 'rejected'
            )
            return render_template('index.html', form=form)

        short_url = URL_map(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(short_url)
        db.session.commit()
        flash(
            url_for(
                'short_link_url', short_id=custom_id, _external=True), 'complete_link'
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=('GET',))
def short_link_url(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)

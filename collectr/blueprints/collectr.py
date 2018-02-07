from sqlite3 import dbapi2 as sqlite3
from flask import Blueprint
from flask import jsonify
from flask import g
from flask import render_template
from flask import current_app
from flask import request
from flask_paginate import Pagination

bp = Blueprint('collectr', __name__)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def get_total_entries(qs=''):
    db = get_db()
    if not qs:
        cur = db.execute('SELECT * FROM sparkmodel')
    else:
        qs = '%%%s%%' % qs
        cur = db.execute('SELECT * FROM sparkmodel '
                         'WHERE upper(title) LIKE ? '
                         'OR upper(product_id) LIKE ?', (qs, qs))
    return len(cur.fetchall())


def get_entries_for_page(page):
    """Returns the paginated database entries."""
    limit = current_app.config['ENTRIES_PER_PAGE']
    offset = (page - 1) * limit
    db = get_db()
    cur = db.execute('SELECT * FROM sparkmodel '
                     'ORDER BY product_id ASC '
                     'LIMIT ? OFFSET ?', (limit, offset))
    return cur.fetchall()


def get_entries_in_collection():
    db = get_db()
    cur = db.execute('SELECT * FROM sparkmodel '
                     'WHERE in_collection = 1 '
                     'ORDER BY product_id ASC ')
    return cur.fetchall()

def get_qs_result_for_page(qs, page):
    limit = current_app.config['ENTRIES_PER_PAGE']
    offset = (page - 1) * limit
    db = get_db()
    qs = '%%%s%%' % qs
    cur = db.execute('SELECT * FROM sparkmodel '
                     'WHERE upper(title) LIKE ? OR upper(product_id) LIKE ? '
                     'ORDER BY product_id ASC '
                     'LIMIT ? OFFSET ?', (qs, qs, limit, offset))
    return cur.fetchall()


@bp.route('/')
def show_entries():
    count = get_total_entries()
    page = int(request.args.get('page', 1))
    entries = get_entries_for_page(page)
    pagination = Pagination(page=page,
                            total=count, css_framework='bootstrap4',
                            per_page=current_app.config['ENTRIES_PER_PAGE'])
    return render_template('show_entries.html', entries=entries,
                           count=count, pagination=pagination)


@bp.route('/search/')
def search():
    qs = request.args.get('query', None)
    count = get_total_entries(qs)
    page = int(request.args.get('page', 1))
    entries = get_qs_result_for_page(qs, page)
    return render_template('show_entries.html',
                           entries=entries, count=count, qs=qs)


@bp.route('/add/')
def add_entry():
    product_id = request.args.get('product_id', None)
    if not product_id:
        result = 'error'
    else:
        db = get_db()
        db.execute('UPDATE sparkmodel '
                   'SET in_collection = ? '
                   'WHERE product_id = ?', (True, product_id))
        db.commit()
        result = 'ok'
    return jsonify(result)


@bp.route('/delete/')
def delete_entry():
    product_id = request.args.get('product_id', None)
    if not product_id:
        result = 'error'
    else:
        db = get_db()
        db.execute('UPDATE sparkmodel '
                   'SET in_collection = ? '
                   'WHERE product_id = ?', (False, product_id))
        db.commit()
        result = 'ok'
    return jsonify(result)


@bp.route('/profile')
def view_profile():
    entries = get_entries_in_collection()
    return render_template('show_profile.html', entries=entries)

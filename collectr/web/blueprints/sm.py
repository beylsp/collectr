from flask import Blueprint
from flask import jsonify
from flask import g
from flask import render_template
from flask import current_app
from flask import request
from flask_paginate import Pagination
from sqlalchemy import asc
from sqlalchemy import or_
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from collectr.db.models import SparkModelData

bp = Blueprint('sm', __name__)


def connect_db():
    engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    db = scoped_session(sessionmaker(autocommit=False,
                                     autoflush=False,
                                     bind=engine))
    return db


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db


def get_total_entries(qs=''):
    db = get_db()
    if not qs:
        result = db.query(SparkModelData).all()
    else:
        qs = '%%%s%%' % qs
        result = db.query(SparkModelData).filter(or_(
                SparkModelData.title.ilike(qs),
                SparkModelData.product_id.ilike(qs))).all()
    return len(result)


def get_entries_for_page(page):
    """Returns the paginated database entries."""
    limit = current_app.config['ENTRIES_PER_PAGE']
    offset = (page - 1) * limit
    db = get_db()
    result = db.query(SparkModelData).order_by(
            asc(SparkModelData.product_id)).offset(offset).limit(limit).all()
    return result


def get_entries_in_collection():
    db = get_db()
    result = db.query(SparkModelData).filter(
            SparkModelData.in_collection == 1).order_by(asc(SparkModelData.product_id)).all()
    return result


def get_qs_result_for_page(qs, page):
    limit = current_app.config['ENTRIES_PER_PAGE']
    offset = (page - 1) * limit
    db = get_db()
    qs = '%%%s%%' % qs
    result = db.query(SparkModelData).filter(or_(
            SparkModelData.title.like(qs), SparkModelData.product_id.like(qs))).order_by(
                    asc(SparkModelData.product_id)).limit(limit).offset(offset).all()
    return result


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
    pagination = Pagination(page=page,
                            total=count, css_framework='bootstrap4',
                            per_page=current_app.config['ENTRIES_PER_PAGE'])
    return render_template('show_entries.html', pagination=pagination,
                           entries=entries, count=count, qs=qs)


@bp.route('/add/')
def add_entry():
    product_id = request.args.get('product_id', None)
    if not product_id:
        result = 'error'
    else:
        db = get_db()
        db.query(SparkModelData).filter(SparkModelData.product_id == product_id).update({'in_collection': 1})
        db.commit()
        result = 'ok'
    return jsonify(result=result)


@bp.route('/delete/')
def delete_entry():
    product_id = request.args.get('product_id', None)
    if not product_id:
        result = 'error'
    else:
        db = get_db()
        db.query(SparkModelData).filter(SparkModelData.product_id == product_id).update({'in_collection': 0})
        db.commit()
        result = 'ok'
    return jsonify(result=result)


@bp.route('/profile')
def view_profile():
    entries = get_entries_in_collection()
    return render_template('show_profile.html', entries=entries)

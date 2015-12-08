from flask import Blueprint

products = Blueprint('products', __name__)


@products.route('/products')
def show_products():
    return 'my products'

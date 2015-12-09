"""Blueprint module that associates product view functions."""
from flask import Blueprint

products = Blueprint('products', __name__)


@products.route('/products')
def show_products():
    """Show all products."""
    return 'my products'

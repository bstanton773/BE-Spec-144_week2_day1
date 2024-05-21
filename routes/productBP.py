from flask import Blueprint
from controllers.productController import save

product_blueprint = Blueprint('product_bp', __name__)

def placeholder2():
    return 'This is a placeholder 2'

product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(placeholder2)

from flask import Flask
from database import db
from schemas import ma
from limiter import limiter

from models.customer import Customer
from models.customerAccount import CustomerAccount

from routes.customerBP import customer_blueprint


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)

    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')

def config_rate_limit():
    limiter.limit("10 per hour")(customer_blueprint)

if __name__ == "__main__":
    app = create_app('DevelopmentConfig')

    blueprint_config(app)
    config_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True, port=8888)

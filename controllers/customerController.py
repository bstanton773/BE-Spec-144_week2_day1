from flask import request, jsonify
from schemas.customerSchema import customer_input_schema, customer_output_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache


def save():
    try:
        # Validate and deserialize the request data
        customer_data = customer_input_schema.load(request.json)
        customer_save = customerService.save(customer_data)
        return customer_output_schema.jsonify(customer_save), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({"error": str(err)}), 400



@cache.cached(timeout=60)
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200

from flask import request, jsonify
from schemas.customerSchema import customer_schema
from services import customerService
from marshmallow import ValidationError


def save():
    try:
        # Validaate and deserialize the request data
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Call the save service with the customer data
    customer_save = customerService.save(customer_data)
    # Serialize the customer data and return with a 201 success
    return customer_schema.jsonify(customer_save), 201

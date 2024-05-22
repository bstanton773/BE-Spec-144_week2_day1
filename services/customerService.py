from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.customer import Customer
from circuitbreaker import circuit
from werkzeug.security import generate_password_hash


# Fallback function - executed once the limit has been passed
def fallback_func(customer_data):
    print('The fallback function is being executed')
    return None


# # Create a function that takes in customer data and creates a new customer in db
# @circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
# def save(customer_data):
#     try:
#         if customer_data['name'] == 'Failure':
#             raise Exception("Failure condition triggered") # Raise an exception to simulate failure
#         # Open a session
#         with Session(db.engine) as session:
#             with session.begin():
#                 # Create a new instance of Customer
#                 new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=generate_password_hash(customer_data['password']))
#                 # Add and commit to the database
#                 session.add(new_customer)
#                 session.commit()
#             # After committing the session, the new_customer object may have become detatched
#             # Refresh the object to ensure it is still attached to the session
#             session.refresh(new_customer)
#             return new_customer
#     except Exception as e:
#         # If an exception occurs, the circuit breaker will handle it based on configuration
#         raise e

# Create a function that takes in customer data and creates a new customer in db
def save(customer_data):
    # Open a session
    with Session(db.engine) as session:
        with session.begin():
            # Check to see if any customer has that username
            customer_query = select(Customer).where(Customer.username == customer_data['username'])
            customer_check = session.execute(customer_query).scalars().first()
            # If we do find a customer with that username, raise a ValueError
            if customer_check is not None:
                raise ValueError("Customer with that username already exists")
            # Create a new instance of Customer
            new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=generate_password_hash(customer_data['password']))
            # Add and commit to the database
            session.add(new_customer)
            session.commit()
        # After committing the session, the new_customer object may have become detatched
        # Refresh the object to ensure it is still attached to the session
        session.refresh(new_customer)
        return new_customer


# Function to get all of the customers from the db
def find_all():
    query = db.select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers

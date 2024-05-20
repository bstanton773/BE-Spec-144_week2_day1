from sqlalchemy.orm import Session
from database import db
from models.customer import Customer


# Create a function that takes in customer data and creates a new customer in db
def save(customer_data):
    # Open a session
    with Session(db.engine) as session:
        with session.begin():
            # Create a new instance of Customer
            new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
            # Add and commit to the database
            session.add(new_customer)
            session.commit()
        # After committing the session, the new_customer object may have become detatched
        # Refresh the object to ensure it is still attached to the session
        session.refresh(new_customer)
        return new_customer
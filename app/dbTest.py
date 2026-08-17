from sqlalchemy import text
from app.database import engine
from app.models.customer import Customer
from app.services.customer_service import register_customer, email_customer_one

"""
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())
"""

"""
customer = Customer(
    name = "Veli Bil",
    email = "veli@mail.com",
    password = "12345"
)
register_customer(customer)
"""

customer = email_customer_one("ali@mail.com")
print(f"{customer.id} - {customer.name} - {customer.email}")
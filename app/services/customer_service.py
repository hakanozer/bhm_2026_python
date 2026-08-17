from sqlalchemy import select

from app.database import SessionLocal
from app.models.customer import Customer

# Customer Register fonksiyon
def register_customer(customer: Customer) -> Customer | None:
    with SessionLocal() as session:        
        try:
            session.add(customer)
            session.commit()
            session.refresh(customer)
            
            print(customer.id)
            return customer
        except:
            print("email already exists.")
            return None
        

def email_customer_one(email: str) -> Customer | None:
      with SessionLocal() as session:
          result = select(Customer).where(
              Customer.email == email
          )
          customer = session.scalar(result)
          return customer

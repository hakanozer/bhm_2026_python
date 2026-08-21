from sqlalchemy import select
from app.dtos.customerLoginDto import CustomerLoginDto
from app.database import SessionLocal
from app.dtos.customerRegiserDto import CustomerRegisterDto
from app.models.customer import Customer
from app.dtos.customerLoginResponseDto import CustomerLoginResponseDto


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


def customerLogin(customerLoginDto: CustomerLoginDto) -> CustomerLoginResponseDto | None:
    with SessionLocal() as session:
        resultQuery = select(Customer).where(
            Customer.email == customerLoginDto.email
        )
        customer = session.scalar(resultQuery)
        if customer:
            if customer.password == customerLoginDto.password:
                customer_response = CustomerLoginResponseDto.model_validate(customer)
                return customer_response
            else:
                return None
        else:
            return None
        

def customer_update(id: int, customerRegisterDto: CustomerRegisterDto) -> Customer | None:
    with SessionLocal() as session:
        customer = session.get(Customer, id)
        if customer:
            customer.name = customerRegisterDto.name
            customer.email = customerRegisterDto.email
            customer.password = customerRegisterDto.password
            session.commit()
            session.refresh(customer)
            return customer
        else:
            return None
    
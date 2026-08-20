from fastapi import APIRouter
from app.dtos.customerRegiserDto import CustomerRegisterDto
from app.models.customer import Customer
from app.services.customer_service import register_customer

customerRouter = APIRouter()

@customerRouter.post("/register")
def register(customerRegisterDto: CustomerRegisterDto):
    customer = Customer(
        name=customerRegisterDto.name,
        email=customerRegisterDto.email,
        password=customerRegisterDto.password
    )
    registered_customer = register_customer(customer)
    if registered_customer:
        return {"message": "Customer registered successfully", "customer_id": registered_customer.id}
    else:
        return {"message": "Email already exists."}
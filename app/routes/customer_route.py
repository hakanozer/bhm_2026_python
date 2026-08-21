from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dtos.customerLoginDto import CustomerLoginDto
from app.dtos.customerRegiserDto import CustomerRegisterDto
from app.models.customer import Customer
from app.services.customer_service import customer_update, register_customer, customerLogin

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
        return JSONResponse({"message": "Email already exists."}, 400)
    
    
@customerRouter.post("/login")
def login(customerLoginDto: CustomerLoginDto):
    customer = customerLogin(customerLoginDto)
    if customer:
        return {"message": "Login successful", "customer": customer}
    else:
        return JSONResponse( {"message": "Invalid email or password."}, 400 )
    

@customerRouter.put("/update/{id}")
def update_customer(id: int, customerRegisterDto: CustomerRegisterDto):
    customer = customer_update(id, customerRegisterDto)
    if customer:
        return {"message": "Customer updated successfully", "customer": customer}
    else:
        return JSONResponse({"message": "Customer not found."}, 404)
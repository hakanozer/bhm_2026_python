from fastapi import FastAPI
from app.routes.customer_route import customerRouter

app = FastAPI()

# router ekleme
app.include_router(customerRouter, prefix="/customer")
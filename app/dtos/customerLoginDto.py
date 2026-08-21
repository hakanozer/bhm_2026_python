from pydantic import BaseModel

class CustomerLoginDto(BaseModel):
    email: str
    password: str
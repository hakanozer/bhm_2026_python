from pydantic import BaseModel

class CustomerRegisterDto(BaseModel):
    name: str
    email: str
    password: str
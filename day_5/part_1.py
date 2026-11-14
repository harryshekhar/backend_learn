from pydantic import BaseModel

class user(BaseModel):
    id : int
    name:str 
    is_active : bool

input_data ={"id" : 101 , "name " : "shekhar " 'is_active': 
             True}

user = user()

from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0, description="Must be greater than 0")
    stock: int = Field(default=0, ge=0)  
    sku: str = Field(..., pattern=r"^[A-Z]{3}-\d{3}$") 

item = Product(name="Wireless Mouse", price=24.99, sku="LOG-402")



from datetime import date
from pydantic import BaseModel, EmailStr, HttpUrl

class Employee(BaseModel):
    full_name: str
    work_email: EmailStr
    portfolio_url: HttpUrl | None = None
    joining_date: date

emp = Employee(
    full_name="shekhar",
    work_email="shekhar@company.com",
    portfolio_url="https://shekhar.dev",
    joining_date="2026-11-15",
)


from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pincode: str

class Customer(BaseModel):
    name: str
    address: Address        
    tags: list[str] = []      

customer = Customer(
    name="Rohan",
    address={"city": "Mumbai", "pincode": "400001"},
    tags=["vip", "prime"],
)
print(customer.address.city) 



from pydantic import BaseModel, field_validator

class SignupForm(BaseModel):
    username: str
    password: str

    @field_validator("username")
    @classmethod
    def clean_username(cls, v: str) -> str:
        if " " in v:
            raise ValueError("Username cannot contain spaces")
        return v.lower().strip()

    @field_validator("password")
    @classmethod
    def check_password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v

form = SignupForm(username="  DevUser99 ", password="supersecret123")
print(form.username) 
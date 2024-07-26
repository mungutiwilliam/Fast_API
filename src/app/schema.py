# build a schema using pydantic
from pydantic import BaseModel


class Categories(BaseModel):
    category_id: int
    category_department_id: int
    category_name: str

    class Config:
        from_attributes = True


class Customers(BaseModel):
    customer_id: int
    customer_fname: str
    customer_lname: str
    customer_email: str
    customer_password: str
    customer_street: str
    customer_city: str
    customer_state: str
    customer_zipcode: str

    class Config:
        from_attributes = True


class Departments(BaseModel):
    department_id: int
    department_name: str

    class Config:
        from_attributes = True

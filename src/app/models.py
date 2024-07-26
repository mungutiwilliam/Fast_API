from sqlalchemy import (
    Column,
    # DateTime,
    # ForeignKey,
    Integer,
    String,
    # Float
                        )
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True, index=True)
    category_department_id = Column(Integer)
    category_name = Column(String)


class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    customer_fname = Column(String)
    customer_lname = Column(String)
    customer_email = Column(String)
    customer_password = Column(String)
    customer_street = Column(String)
    customer_city = Column(String)
    customer_state = Column(String)
    customer_zipcode = Column(String)


class Departments(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String)

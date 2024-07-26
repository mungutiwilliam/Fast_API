import uvicorn
import os
from fastapi import FastAPI, HTTPException, Path

from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Categories as SchemaCat
from schema import Customers as SchemaCust
from schema import Departments as SchemaDepart

from models import Categories as ModelCategories
from models import Customers as ModelCustomers
from models import Departments as ModelDepartments

load_dotenv('../.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post('/new_department/', response_model=SchemaDepart)
async def new_department(department: SchemaDepart):
    try:
        db_department = ModelDepartments(
            department_id=department.department_id,
            department_name=department.department_name
        )
        print(db_department)

        db.session.add(db_department)
        db.session.commit()
        return db_department
    except Exception as e:
        print('Id already exists in the database')
        raise HTTPException(status_code=400, detail="Id already exists in the database")


@app.put('/edit_department/{dep_id}', response_model=SchemaDepart)
async def edit_department(payload: SchemaDepart, dep_id: int = Path(...)):
    try:
        department_query = await (
            db.session.query(payload).
            filter(payload.department_id == dep_id))

        print('Department_query', department_query)
        found_department = department_query.scalar_one_or_none()
        if not found_department:
            raise HTTPException(status_code=404, detail="Department not found")

        found_department = department_query.first()
        db.session.add(found_department)
        db.session.commit()
        response_object = {
            "department_id": SchemaDepart.department_id,
            "department_name": payload.department_name
        }
        return response_object
    except Exception as e:
        print('Error occurred:', e)
        raise HTTPException(status_code=500, detail="Internal server error")


# @app.delete('/delete_department/{id}', response_model=SchemaDepart)
# async def delete_department(dep_id: department_id):
#     for department in db:
#         if department.id == department_id:
#             db.remove(department)
#     db_department = ModelDepartments(
#         department_id=department.id,
#         department_name=department.department_name
#     )
#     db.session.add(db_department)
#     db.session.commit()
#     return db_department


@app.delete('/delete_department/', response_model=SchemaDepart)
async def new_department(department: SchemaDepart):
    try:
        try:
            db_department = ModelDepartments(
                department_id=department.id,
                department_name=department.department_name
            )
            db.session.add(db_department)
            db.session.commit()
            return db_department
        except Exception as e:
            raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        print('Error:', e)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.post('/new_category/', response_model=SchemaCat)
async def new_category(category: SchemaCat):
    try:
        db_category = ModelCategories(
            category_id=category.category_id,
            category_department_id=category.category_department_id,
            category_name=category.category_name
        )
        db.session.add(db_category)
        db.session.commit()
        return db_category
    except Exception as e:
        print('Id already exists in the database')
        raise HTTPException(status_code=400, detail="Id already exists in the database")


@app.post('/new_customer/', response_model=SchemaCust)
async def new_customer(customer: SchemaCust):
    try:
        db_customer = ModelCustomers(
            customer_id=customer.customer_id,
            customer_fname=customer.customer_fname,
            customer_lname=customer.customer_lname,
            customer_email=customer.customer_email,
            customer_password=customer.customer_password,
            customer_street=customer.customer_street,
            customer_city=customer.customer_city,
            customer_state=customer.customer_state,
            customer_zipcode=customer.customer_zipcode
        )
        db.session.add(db_customer)
        db.session.commit()
        return db_customer
    except Exception:
        print('Id already exists in the database')
        raise HTTPException(status_code=400, detail="Id already exists in the database")


@app.get('/customers/')
async def customers():
    try:
        customers_all = db.session.query(ModelCustomers).all()
        return customers_all
    except Exception:
        print('Error occurred while retrieving records:', e)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get('/categories/')
async def categories():
    try:
        categories_all = db.session.query(ModelCategories).all()
        return categories_all
    except Exception as e:
        print('Error occurred while retrieving records:', e)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get('/departments/')
async def departments():
    try:
        departments_all = db.session.query(ModelDepartments).all()
        return departments_all
    except Exception as e:
        print('Error occurred while retrieving records:', e)
        raise HTTPException(status_code=500, detail="Internal server error")


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8002)

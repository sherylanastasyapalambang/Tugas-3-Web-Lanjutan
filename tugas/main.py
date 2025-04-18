from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

# Import model CRUD and schemas
import crud.productlines as productline_crud
import schemas.productlines as productline_schema

import crud.products as product_crud
import schemas.products as product_schema

import crud.employees as employee_crud
import schemas.employees as employee_schema

import crud.customers as customer_crud
import schemas.customers as customer_schema

from models.products import Product
from models.productlines import ProductLines


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency untuk session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================
# PRODUCTLINES ENDPOINTS
# ============================
# Get all product lines
@app.get("/productlines", response_model=list[productline_schema.ProductLine])
def get_all_productlines(db: Session = Depends(get_db)):
    return productline_crud.get_all(db)

# Get one product line by id
@app.get("/productlines/{id}", response_model=productline_schema.ProductLine)
def get_one_productline(id: str, db: Session = Depends(get_db)):
    result = productline_crud.get_one(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

# Create a product line
@app.post("/productlines/{id}", response_model=productline_schema.ProductLine)
def create_productline(id: str, data: productline_schema.ProductLineCreate, db: Session = Depends(get_db)):
    return productline_crud.create(db, id, data)

# Delete a product line
@app.delete("/productlines/{id}")
def delete_productline(id: str, db: Session = Depends(get_db)):
    result = productline_crud.delete(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ============================
# PRODUCTS ENDPOINTS
# ============================

@app.get("/products", response_model=list[product_schema.Product])
def get_all_products(db: Session = Depends(get_db)):
    return product_crud.get_all(db)

@app.get("/products/{code}", response_model=product_schema.Product)
def get_one_product(code: str, db: Session = Depends(get_db)):
    result = product_crud.get_one(db, code)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@app.post("/products/{code}", response_model=product_schema.Product)
def create_product(code: str, data: product_schema.ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create(db, code, data)

@app.delete("/products/{code}")
def delete_product(code: str, db: Session = Depends(get_db)):
    result = product_crud.delete(db, code)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ============================
# EMPLOYEES ENDPOINTS
# ============================

@app.get("/employees", response_model=list[employee_schema.Employee])
def get_all_employees(db: Session = Depends(get_db)):
    return employee_crud.get_all(db)

@app.get("/employees/{id}", response_model=employee_schema.Employee)
def get_one_employee(id: int, db: Session = Depends(get_db)):
    result = employee_crud.get_one(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@app.post("/employees/{id}", response_model=employee_schema.Employee)
def create_employee(id: int, data: employee_schema.EmployeeCreate, db: Session = Depends(get_db)):
    return employee_crud.create(db, id, data)

@app.delete("/employees/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    result = employee_crud.delete(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ============================
# CUSTOMERS ENDPOINTS
# ============================

@app.get("/customers", response_model=list[customer_schema.Customer])
def get_all_customers(db: Session = Depends(get_db)):
    return customer_crud.get_all(db)

@app.get("/customers/{id}", response_model=customer_schema.Customer)
def get_one_customer(id: int, db: Session = Depends(get_db)):
    result = customer_crud.get_one(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@app.post("/customers/{id}", response_model=customer_schema.Customer)
def create_customer(id: int, data: customer_schema.CustomerCreate, db: Session = Depends(get_db)):
    return customer_crud.create(db, id, data)

@app.delete("/customers/{id}")
def delete_customer(id: int, db: Session = Depends(get_db)):
    result = customer_crud.delete(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

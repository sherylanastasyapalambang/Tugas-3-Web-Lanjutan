from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

# Import model CRUD and schemas
import crud.productlines as productline_crud
import schemas.productlines as productline_schema

import crud.products as product_crud
import schemas.products as product_schema

import crud.offices as office_crud
import schemas.offices as office_schema

import crud.employees as employee_crud
import schemas.employees as employee_schema

import crud.customers as customer_crud
import schemas.customers as customer_schema

import crud.orderdetails as od_crud
import schemas.orderdetails as od_schema

import crud.orders as order_crud
import schemas.orders as order_schema

import crud.payments as payment_crud
import schemas.payments as payment_schema


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

# Update a product line
@app.put("/productlines/{id}", response_model=productline_schema.ProductLine)
def update_productline(id: str, data: productline_schema.ProductLineCreate, db: Session = Depends(get_db)):
    result = productline_crud.update(db, id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

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
def read_products(db: Session = Depends(get_db)):
    return product_crud.get_all_products(db)

@app.get("/products/{productCode}", response_model=product_schema.Product)
def read_product(productCode: str, db: Session = Depends(get_db)):
    db_product = product_crud.get_product_by_code(db, productCode)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.post("/products", response_model=product_schema.Product)
def create_product(product: product_schema.ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create_product(db, product)

@app.put("/products/{productCode}", response_model=product_schema.Product)
def update_product(productCode: str, product: product_schema.ProductUpdate, db: Session = Depends(get_db)):
    db_product = product_crud.update_product(db, productCode, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/products/{productCode}", response_model=product_schema.Product)
def delete_product(productCode: str, db: Session = Depends(get_db)):
    db_product = product_crud.delete_product(db, productCode)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# ============================
# OFFICES ENDPOINTS
# ============================
@app.get("/offices", response_model=list[office_schema.Office])
def read_offices(db: Session = Depends(get_db)):
    return office_crud.get_all(db)

@app.get("/offices/{officeCode}", response_model=office_schema.Office)
def read_office(officeCode: str, db: Session = Depends(get_db)):
    office = office_crud.get_one(db, officeCode)
    if not office:
        raise HTTPException(status_code=404, detail="Office not found")
    return office

@app.post("/offices", response_model=office_schema.Office)
def create_office(data: office_schema.OfficeCreate, db: Session = Depends(get_db)):
    return office_crud.create(db, data)

@app.put("/offices/{officeCode}", response_model=office_schema.Office)
def update_office(officeCode: str, data: office_schema.OfficeCreate, db: Session = Depends(get_db)):
    result = office_crud.update(db, officeCode, data)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@app.delete("/offices/{officeCode}")
def delete_office(officeCode: str, db: Session = Depends(get_db)):
    result = office_crud.delete(db, officeCode)
    if not result:
        raise HTTPException(status_code=404, detail="Office not found")
    return {"ok": True}


# ============================
# EMPLOYEES ENDPOINTS
# ============================
@app.get("/employees", response_model=list[employee_schema.Employee])
def read_employees(db: Session = Depends(get_db)):
    return employee_crud.get_all(db)

@app.get("/employees/{employeeNumber}", response_model=employee_schema.Employee)
def read_employee(employeeNumber: int, db: Session = Depends(get_db)):
    employee = employee_crud.get_one(db, employeeNumber)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.post("/employees", response_model=employee_schema.Employee)
def create_employee(data: employee_schema.EmployeeCreate, db: Session = Depends(get_db)):
    return employee_crud.create(db, data.employeeNumber, data)

@app.put("/employees/{employeeNumber}", response_model=employee_schema.Employee)
def update_employee(employeeNumber: int, data: employee_schema.EmployeeCreate, db: Session = Depends(get_db)):
    # Memastikan bahwa update menerima data yang benar dan fungsi update di CRUD menangani update sesuai
    result = employee_crud.update(db, employeeNumber, data)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result


@app.delete("/employees/{employeeNumber}")
def delete_employee(employeeNumber: int, db: Session = Depends(get_db)):
    result = employee_crud.delete(db, employeeNumber)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"ok": True}

# ============================
# CUSTOMERS ENDPOINTS
# ============================


@app.get("/customers", response_model=list[customer_schema.Customer])
def read_customers(db: Session = Depends(get_db)):
    return customer_crud.get_all(db)

@app.get("/customers/{customerNumber}", response_model=customer_schema.Customer)
def read_customer(customerNumber: int, db: Session = Depends(get_db)):
    customer = customer_crud.get_one(db, customerNumber)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.post("/customers", response_model=customer_schema.Customer)
def create_customer(data: customer_schema.CustomerCreate, db: Session = Depends(get_db)):
    return customer_crud.create(db, data)

@app.put("/customers/{customerNumber}", response_model=customer_schema.Customer)
def update_customer(customerNumber: int, data: customer_schema.CustomerCreate, db: Session = Depends(get_db)):
    result = customer_crud.update(db, customerNumber, data)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return result

@app.delete("/customers/{customerNumber}")
def delete_customer(customerNumber: int, db: Session = Depends(get_db)):
    result = customer_crud.delete(db, customerNumber)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"ok": True}


# ============================
# ORDER DETAILS ENDPOINTS
# ============================

@app.get("/orderdetails", response_model=list[od_schema.OrderDetail])
def read_orderdetails(db: Session = Depends(get_db)):
    return od_crud.get_all_orderdetails(db)

@app.get("/orderdetails/{orderNumber}/{productCode}", response_model=od_schema.OrderDetail)
def read_orderdetail(orderNumber: int, productCode: str, db: Session = Depends(get_db)):
    od = od_crud.get_orderdetail(db, orderNumber, productCode)
    if not od:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return od

@app.post("/orderdetails", response_model=od_schema.OrderDetail)
def create_orderdetail(od: od_schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return od_crud.create_orderdetail(db, od)

@app.put("/orderdetails/{orderNumber}/{productCode}", response_model=od_schema.OrderDetail)
def update_orderdetail(orderNumber: int, productCode: str, od: od_schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    updated = od_crud.update_orderdetail(db, orderNumber, productCode, od)
    if not updated:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return updated

@app.delete("/orderdetails/{orderNumber}/{productCode}", response_model=od_schema.OrderDetail)
def delete_orderdetail(orderNumber: int, productCode: str, db: Session = Depends(get_db)):
    deleted = od_crud.delete_orderdetail(db, orderNumber, productCode)
    if not deleted:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return deleted


# ============================
# ORDER ENDPOINTS
# ============================
@app.get("/orders", response_model=list[order_schema.Order])
def read_orders(db: Session = Depends(get_db)):
    return order_crud.get_all_orders(db)

@app.get("/orders/{orderNumber}", response_model=order_schema.Order)
def read_order(orderNumber: int, db: Session = Depends(get_db)):
    order = order_crud.get_order(db, orderNumber)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.post("/orders", response_model=order_schema.Order)
def create_order(order: order_schema.OrderCreate, db: Session = Depends(get_db)):
    return order_crud.create_order(db, order)


@app.put("/orders/{orderNumber}", response_model=order_schema.Order)
def update_order(orderNumber: int, order: order_schema.OrderUpdate, db: Session = Depends(get_db)):
    updated = order_crud.update_order(db, orderNumber, order)
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@app.delete("/orders/{orderNumber}", response_model=order_schema.Order)
def delete_order(orderNumber: int, db: Session = Depends(get_db)):
    deleted = order_crud.delete_order(db, orderNumber)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return deleted

# ============================
# PAYMENTS ENDPOINTS
# ============================

@app.get("/payments", response_model=list[payment_schema.Payment])
def read_payments(db: Session = Depends(get_db)):
    return payment_crud.get_all(db)

@app.get("/payments/{customerNumber}/{checkNumber}", response_model=payment_schema.Payment)
def read_payment(customerNumber: int, checkNumber: str, db: Session = Depends(get_db)):
    payment = payment_crud.get_one(db, customerNumber, checkNumber)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.post("/payments", response_model=payment_schema.Payment)
def create_payment(data: payment_schema.PaymentCreate, db: Session = Depends(get_db)):
    return payment_crud.create(db, data)

@app.put("/payments/{customerNumber}/{checkNumber}", response_model=payment_schema.Payment)
def update_payment(customerNumber: int, checkNumber: str, data: payment_schema.PaymentCreate, db: Session = Depends(get_db)):
    result = payment_crud.update(db, customerNumber, checkNumber, data)
    if not result:
        raise HTTPException(status_code=404, detail="Payment not found")
    return result

@app.delete("/payments/{customerNumber}/{checkNumber}")
def delete_payment(customerNumber: int, checkNumber: str, db: Session = Depends(get_db)):
    result = payment_crud.delete(db, customerNumber, checkNumber)
    if not result:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"ok": True}
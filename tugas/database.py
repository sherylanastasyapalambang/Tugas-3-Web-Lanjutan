# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ganti sesuai konfigurasi MySQL/MariaDB kamu
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/classicmodels"

# Membuat engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Membuat session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base untuk model ORM
Base = declarative_base()

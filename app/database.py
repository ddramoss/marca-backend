from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cambia la URL si quieres usar SQLite en un archivo específico de PythonAnywhere
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # o "/home/usuario/nombre.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:////home/diegoramos13/test.db"

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Función helper para crear tablas si no existen
def init_db():
    Base.metadata.create_all(bind=engine)

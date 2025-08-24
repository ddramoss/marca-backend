from sqlalchemy import Column, Integer, String
from .database import Base  # Ajusta la importación si lo subes a PythonAnywhere

class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(200), nullable=False)
    titular = Column(String(200), nullable=False)
    estado = Column(String(200), nullable=False)  # "Activo" o "Inactivo"

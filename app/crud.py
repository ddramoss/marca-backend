from .models import Brand
from .database import SessionLocal

# Helper para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todas las marcas
def get_brands():
    db = next(get_db())
    return db.query(Brand).all()

# Obtener marca por ID
def get_brand(brand_id):
    db = next(get_db())
    return db.query(Brand).filter(Brand.id == brand_id).first()

# Crear marca
def create_brand(data):
    db = next(get_db())
    db_brand = Brand(**data)  # data es un dict con los campos de Brand
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

# Actualizar marca
def update_brand(brand_id, data):
    db = next(get_db())
    db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if db_brand:
        for key, value in data.items():
            setattr(db_brand, key, value)
        db.commit()
        db.refresh(db_brand)
    return db_brand

# Eliminar marca
def delete_brand(brand_id):
    db = next(get_db())
    db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if db_brand:
        db.delete(db_brand)
        db.commit()
    return db_brand

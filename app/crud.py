from sqlalchemy.orm import Session
from . import models, schemas

def get_brands(db: Session):
    return db.query(models.Brand).all()

def get_brand(db: Session, brand_id: int):
    return db.query(models.Brand).filter(models.Brand.id == brand_id).first()

def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(**brand.dict())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

def update_brand(db: Session, brand_id: int, brand: schemas.BrandUpdate):
    db_brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if db_brand:
        for key, value in brand.dict().items():
            setattr(db_brand, key, value)
        db.commit()
        db.refresh(db_brand)
    return db_brand

def delete_brand(db: Session, brand_id: int):
    db_brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if db_brand:
        db.delete(db_brand)
        db.commit()
    return db_brand

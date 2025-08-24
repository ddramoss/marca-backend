from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter(prefix="/brands", tags=["brands"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.BrandOut])
def list_brands(db: Session = Depends(get_db)):
    return crud.get_brands(db)

@router.post("/", response_model=schemas.BrandOut)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    return crud.create_brand(db, brand)

@router.put("/{brand_id}", response_model=schemas.BrandOut)
def update_brand(brand_id: int, brand: schemas.BrandUpdate, db: Session = Depends(get_db)):
    db_brand = crud.update_brand(db, brand_id, brand)
    if not db_brand:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_brand

@router.delete("/{brand_id}")
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.delete_brand(db, brand_id)
    if not db_brand:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return {"ok": True}

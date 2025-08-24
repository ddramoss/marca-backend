from pydantic import BaseModel

class BrandBase(BaseModel):
    marca: str
    titular: str
    estado: str

class BrandCreate(BrandBase):
    pass

class BrandUpdate(BrandBase):
    pass

class BrandOut(BrandBase):
    id: int

    class Config:
        orm_mode = True

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from . import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Configurar CORS para que React pueda hacer fetch
origins = [
    "http://localhost:3000",  # desarrollo
    "https://tu-frontend.netlify.app"  # producción
]

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

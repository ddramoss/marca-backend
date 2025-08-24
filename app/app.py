from flask import Flask
from flask_cors import CORS
from .database import init_db
from .routes import brands_bp  # Tu blueprint adaptado de rutas

# Inicializar la base de datos
init_db()

app = Flask(__name__)

# Configurar CORS para React
origins = [
    "http://localhost:3000",  # desarrollo
    "https://tu-frontend.vercel.app"  # producción
]
CORS(app, origins=origins)

# Registrar blueprint de rutas
app.register_blueprint(brands_bp)

if __name__ == "__main__":
    app.run(debug=True)

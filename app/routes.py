from flask import Blueprint, jsonify, request
from .crud import get_brands, get_brand, create_brand, update_brand, delete_brand

brands_bp = Blueprint('brands', __name__, url_prefix='/brands')

# Obtener todas las marcas
@brands_bp.route('/', methods=['GET'])
def list_brands():
    brands = get_brands()
    # Convertir a lista de dicts para JSON
    result = [b.__dict__ for b in brands]
    for b in result:
        b.pop('_sa_instance_state', None)  # Eliminar objeto interno de SQLAlchemy
    return jsonify(result)

# Crear una marca
@brands_bp.route('/', methods=['POST'])
def add_brand():
    data = request.json
    brand = create_brand(data)
    result = brand.__dict__
    result.pop('_sa_instance_state', None)
    return jsonify(result), 201

# Actualizar una marca
@brands_bp.route('/<int:brand_id>', methods=['PUT'])
def edit_brand(brand_id):
    data = request.json
    brand = update_brand(brand_id, data)
    if not brand:
        return jsonify({"error": "Marca no encontrada"}), 404
    result = brand.__dict__
    result.pop('_sa_instance_state', None)
    return jsonify(result)

# Eliminar una marca
@brands_bp.route('/<int:brand_id>', methods=['DELETE'])
def remove_brand(brand_id):
    brand = delete_brand(brand_id)
    if not brand:
        return jsonify({"error": "Marca no encontrada"}), 404
    return jsonify({"ok": True})

from flask import Blueprint

# Crie Blueprints para diferentes categorias de rotas
user_bp = Blueprint('user', __name__)

# Importa as rotas de cada módulo
from .user_routes import *

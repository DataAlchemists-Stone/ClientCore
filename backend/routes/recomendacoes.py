from flask import Blueprint, jsonify
from controllers.curso_controller import list_cursos

recomendacoes_bp = Blueprint('recomendacoes', __name__)

@recomendacoes_bp.route('/cursos', methods=['GET'])
def cursos():
    cursos = list_cursos()
    return jsonify(cursos)

from flask import request, Blueprint, Response
from src.shared.auth import Auth
import json


login_bp = Blueprint('loginbp', __name__)


@login_bp.get("/")
def login():
    req_data = request.get_json()
    response = Auth.generate_token(req_data)
    return custom_response(response, 200)


@login_bp.errorhandler(404)
def page_not_found(error):
    return custom_response(error, 404)


@login_bp.errorhandler(500)
def internal_error(error):
    return custom_response(error, 500)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

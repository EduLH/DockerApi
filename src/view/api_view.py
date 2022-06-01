from flask import request, Blueprint, Response
from src.controller.filters import *
from src.shared.auth import Auth
import json


api_bp = Blueprint('apibp', __name__)


@api_bp.get("/")
def home():
    return custom_response("Olá mundo!!", 200)


@api_bp.get("/userId=<int:userId>/quant=<int:quant>")
async def get_by_userid(userId, quant):
    auth_response = Auth.decode_token(request.headers.environ['HTTP_AUTHORIZATION'])
    if auth_response['error']:
        return custom_response(auth_response['error'], 401)
    response = await user_query(userId)
    return custom_response(response.json()[0:quant], 200)


@api_bp.get("/id=<int:id>/quant=<int:quant>")
async def get_by_id(id, quant):
    auth_response = Auth.decode_token(request.headers.environ['HTTP_AUTHORIZATION'])
    if auth_response['error']:
        return custom_response(auth_response['error'], 401)
    response = await id_query(id)
    return custom_response(response.json()[0:quant], 200)


@api_bp.get("/completed=<completed>/quant=<int:quant>")
async def get_by_completed(completed, quant):
    auth_response = Auth.decode_token(request.headers.environ['HTTP_AUTHORIZATION'])
    if auth_response['error']:
        return custom_response(auth_response['error'], 401)
    response = await completed_query(completed)
    return custom_response(response.json()[0:quant], 200)


@api_bp.get("/title=<string:title>/quant=<int:quant>")
async def get_by_title(title, quant):
    auth_response = Auth.decode_token(request.headers.environ['HTTP_AUTHORIZATION'])
    if auth_response['error']:
        return custom_response(auth_response['error'], 401)
    response = await title_query(title)
    return custom_response(response.json()[0:quant], 200)


@api_bp.get("/all")
async def get_full_query():
    req_data = request.get_json()
    auth_response = Auth.decode_token(request.headers.environ['HTTP_AUTHORIZATION'])
    if auth_response['error']:
        return custom_response(auth_response['error'], 401)
    response = await all_query(req_data)
    return custom_response(response.json()[0:req_data['quant']], 200)

@api_bp.get("/alllike")
async def get_full_like():
    req_data = request.get_json()
    auth_response = Auth.decode_token(request.headers.environ['HTTP_AUTHORIZATION'])
    if auth_response['error']:
        return custom_response(auth_response['error'], 401)
    response = await search_like(req_data)
    return custom_response(response[0:req_data['quant']], 200)

@api_bp.route("/pega")
async def get():
    auth_response = Auth.decode_token(request.headers.environ['HTTP_AUTHORIZATION'])
    if auth_response['error']:
        return custom_response(auth_response['error'], 401)
    response = await get_info({})
    return custom_response(response.json()[0:4], 200)


@api_bp.errorhandler(404)
def page_not_found(error):
    return custom_response(error, 404)


@api_bp.errorhandler(500)
def internal_error(error):
    return custom_response(error, 500)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

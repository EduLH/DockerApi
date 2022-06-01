from flask import Flask, json, Response, request
from src.controller.service_consumer import get_info
from src.controller.filters import *
from config import app_config


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )


app = Flask(__name__)
config = (app_config['development'])


@app.get("/")
def home():
    return custom_response("Olá mundo!!", 200)


@app.get("/userId=<int:userId>/quant=<int:quant>")
async def get_by_userid(userId, quant):
    response = await user_query(userId)
    return custom_response(response.json()[0:quant], 200)


@app.get("/id=<int:id>/quant=<int:quant>")
async def get_by_id(id, quant):
    response = await id_query(id)
    return custom_response(response.json()[0:quant], 200)


@app.get("/completed=<completed>/quant=<int:quant>")
async def get_by_completed(completed, quant):
    response = await completed_query(completed)
    return custom_response(response.json()[0:quant], 200)


@app.get("/title=<string:title>/quant=<int:quant>")
async def get_by_title(title, quant):
    response = await title_query(title)
    return custom_response(response.json()[0:quant], 200)


@app.get("/all")
async def get_full_query():
    req_data = request.get_json()
    response = await all_query(req_data)
    return custom_response(response.json()[0:req_data['quant']], 200)

@app.get("/alllike")
async def get_full_like():
    req_data = request.get_json()
    response = await search_like(req_data)
    return custom_response(response[0:req_data['quant']], 200)

@app.route("/pega")
async def get():
    response = await get_info({})
    return custom_response(response.json()[0:4], 200)


@app.errorhandler(404)
def page_not_found(error):
    return custom_response(error, 404)

@app.errorhandler(500)
def internal_error(error):
    return custom_response(error, 500)


if __name__ == '__main__':
    app.run(debug=config.DEBUG,
            host=config.HOST,
            port=config.PORT)

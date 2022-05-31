from flask import Flask, json, Response
from src.controller.service_consumer import get_info
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


@app.post("/int/<int:some_int>")
def int_input(some_int):
    return custom_response(f"Numero {some_int}", 200)


@app.route("/pega")
async def GET():
    response = await get_info()
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

from flask import Flask
from src.controller.service_consumer import get_info

app = Flask(__name__)


@app.get("/")
def home():
    return "Olá mundo!!"


@app.post("/int/<int:some_int>")
def int_input(some_int):
    return f"Numero {some_int}"


@app.route("/pega")
async def GET():
    response = await get_info()
    return response.json()[0:4]


@app.errorhandler(404)
def page_not_found(error):
    return f"error: {error}"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9007)


from flask import Flask
from config import app_config
from src.view.api_view import api_bp as api_blueprint
from src.view.login import login_bp as login_blueprint



app = Flask(__name__)
config = (app_config['development'])

app.register_blueprint(api_blueprint, url_prefix='/')
app.register_blueprint(login_blueprint, url_prefix='/login')


if __name__ == '__main__':
    app.run(debug=config.DEBUG,
            host=config.HOST,
            port=config.PORT)

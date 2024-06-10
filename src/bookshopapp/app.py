from .extensions import db,migrate
from flask import Flask
from .config import DevEnvConfig,Config,ProdEnvConfig,env
from .product.routes import blueprint as product_blueprint




def create_app(config_class=Config):
    newApp = Flask(__name__)
    newApp.config.from_object(config_class)
    db.init_app(newApp)
    migrate.init_app(newApp, db,render_as_batch=True)
    return newApp
app = create_app(DevEnvConfig if env == 'dev' else ProdEnvConfig)
app.register_blueprint(product_blueprint)


@app.route('/index')
def index():
    return {'msg':'Welcome to my app'}



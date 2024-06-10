from dotenv import load_dotenv
import os



basedir = os.path.abspath(os.path.dirname(__file__))
env = os.environ.get('MYENV','dev')
load_dotenv()
class Config:
    pass


class DevEnvConfig(Config):
    db_url = 'sqlite:///'+os.environ.get('DEV_DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = db_url


class ProdEnvConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


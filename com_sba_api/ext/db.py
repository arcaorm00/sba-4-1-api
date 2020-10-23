from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'mariadb'
}

charset = {'utf8': 'utf8'}

url = f'mysql+mysqlconnector://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}?charset=utf8'
Base = declarative_base()
engine = create_engine(url)

def openSession():
    return sessionmaker(bind=engine)
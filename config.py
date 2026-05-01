import os

class Config:
    SECRET_KEY = 'clave-secreta-para-el-proyecto'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reciclaje_quimico.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
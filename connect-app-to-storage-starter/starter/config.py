import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sql-server1015.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-world1015'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'D@t@b@$3123'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'helloworld1015'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'wDYz06sWesf2Edd563vZs59vpvFu5vvnN/y070qqtT8OaQAjj0R6aMWiik4SQ25bcgf6BL7uINAH9Vk2XuR1Ew=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'helloworld1015'

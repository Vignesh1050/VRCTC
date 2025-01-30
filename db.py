import pymysql
from config import DATABASE_CONFIG

def get_db_connection():
    return pymysql.connect(**DATABASE_CONFIG)

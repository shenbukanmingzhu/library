# app/config.py
from dotenv import load_dotenv
import os

# 加载.env 
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:zhiwei520@localhost:3306/library_management"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key')  # 密钥
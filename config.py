import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
print(f'DB_URL: {Config.SQLALCHEMY_DATABASE_URI}')
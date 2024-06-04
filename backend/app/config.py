import os

class Config:
    API_KEY = os.getenv('CURRENCY_API_KEY', 'b1b7fa417c2c9501fe59bcbd')
    BASE_URL = 'https://api.exchangerate-api.com/v4/latest/'
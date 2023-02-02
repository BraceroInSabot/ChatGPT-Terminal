from decouple import config

API_KEY = config("API_KEY", cast=str)
model_engine = "text-davinci-003"

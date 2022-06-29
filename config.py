from distutils.debug import DEBUG
from os import environ as env

DEBUG = env.get("DEBUG", False)
HOST = env.get("HOST", "0.0.0.0")
PORT = env.get("PORT", 5000)
MESSAGE = env.get("MESSAGE", "Hello World!")
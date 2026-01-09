from fastapi import FastAPI

APP=FastAPI()

@APP.get("/")
def ola():
    return "ola mundo"

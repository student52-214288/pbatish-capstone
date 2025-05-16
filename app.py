from fastapi import FastAPI, Depends
import os

app = FastAPI(
    title="Paurush Devops app",
    description="FAST API app for capstone",
    version="1.0.0"
)


def get_settings():
    return {
        "app_name": os.environ.get("APP_NAME", "DevOps Demo App"),
        "author_name": os.environ.get("AUTHOR_NAME", "Pbatish"),
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "secret_key": os.environ.get("SECRET_KEY", "not-so-secret")
    }


@app.get("/health", summary="Health Check")
def health_check():
    return {"status": "OK", "message": "The application is healthy!"}


@app.get("/version", summary="Get App Version")
def get_version():
    return {"version": app.version}


@app.get("/env", summary="Check Environment Variables")
def get_env(settings: dict = Depends(get_settings)):
    return {
        "app_name": settings["app_name"],
        "author_name": settings["author_name"],
        "environment": settings["environment"],
        "secret_key": settings["secret_key"]
    }

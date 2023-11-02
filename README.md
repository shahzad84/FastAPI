# FastAPI

Here are the steps to create a virtual environment and install FastAPI:

## Create Virtual Environment

```bash
pip install virtualenv
virtualenv env
.\env\scripts\activate
```

This will create a virtual environment called `env` and activate it.

## Install FastAPI

```bash 
pip install fastapi
pip install uvicorn

```
## TO RUN the server
```bash
uvicorn app:app --reload
```
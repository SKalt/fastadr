import uvicorn
from fastapi import FastAPI
from .server import api, register_paths

app = FastAPI()
register_paths()
app.include_router(api, prefix="/OpenADR/3.0.1")
uvicorn.run(app, host="0.0.0.0:5000")  # type: ignore

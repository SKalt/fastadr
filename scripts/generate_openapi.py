from fastapi import FastAPI
from src.server import api, register_paths
import yaml

register_paths()
app = FastAPI()
app.include_router(api)

schema = app.openapi()
print(yaml.dump(schema))

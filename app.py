from typing import Optional
import uvicorn
from settings import settings
from api import router

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()
app.include_router(router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# uvicorn.run('app:app', host=settings.server_host, port=settings.server_port, reload=True)


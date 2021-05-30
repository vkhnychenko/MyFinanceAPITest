from api import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

# uvicorn.run('app:app', host=settings.server_host, port=settings.server_port, reload=True)

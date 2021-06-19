import uvicorn
from api import router
from fastapi import FastAPI
from tables import Base
from database import engine
from settings import settings

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authorization'
    }
]

Base.metadata.create_all(bind=engine)

app = FastAPI(title='FinanceAPI', description='trorlolo', version='1.0.0', openapi_tags=tags_metadata)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("app:app", host=settings.server_host, port=settings.server_port, reload=True)

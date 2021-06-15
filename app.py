from api import router
from fastapi import FastAPI

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authorization'
    }
]

app = FastAPI(title='FinanceAPI', description='trorlolo', version='1.0.0', openapi_tags=tags_metadata)
app.include_router(router)

# uvicorn.run('app:app', host=settings.server_host, port=settings.server_port, reload=True)

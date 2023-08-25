from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from to_do.routes import auth, to_dos, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(to_dos.router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def read_root():
    return {'message': 'Hello world'}

from fastapi import FastAPI

from to_do.routes import auth, to_dos, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(to_dos.router)


@app.get('/')
def read_root():
    return {'message': 'Hello world'}

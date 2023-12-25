from Router.userRouter import user
from Router.productRouter import product
from Router.router import compra
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from connection.connection import database,Session


app = FastAPI()

"""
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


"""
app.include_router(user)
app.include_router(product)
app.include_router(compra)
# Configuración de CORS
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)




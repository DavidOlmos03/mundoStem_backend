from Router.userRouter import user
from Router.bookRouter import book
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from connection.connection import database,Session


app = FastAPI()


app.include_router(user)
app.include_router(book)

# Configuración de CORS
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




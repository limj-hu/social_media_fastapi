from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import post, user, auth, vote
from .database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
        allow_credentials=True,
        allow_headers=['*'],
        allow_methods=['*'],
        allow_origins=['*']
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
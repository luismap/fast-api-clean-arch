from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import logging.config
from app.routes import auth, post, user, votes
from core.utils.MyUtils import MyUtils

canlog = True
appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])

app = FastAPI()

origins = [
    "https://mydomain.com",  # useful for cross-origin resource sharin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["get", "post"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    if canlog:
        logger.info("root got call")
    return {"Hello": "World"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

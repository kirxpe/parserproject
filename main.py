from fastapi import FastAPI
from parsing import get_hacker_news_links

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FastAPI first steps"}


@app.get("/links")
async def get_links():
    return {"links": get_hacker_news_links()}

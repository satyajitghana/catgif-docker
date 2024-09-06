import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

TENOR_API_KEY = os.getenv("TENOR_API_KEY")
TENOR_API_URL = "https://tenor.googleapis.com/v2/search"

async def get_cat_gif_url():
    async with httpx.AsyncClient() as client:
        params = {
            "q": "cat",
            "key": TENOR_API_KEY,
            "client_key": "my_test_app",
            "limit": 50,  # Fetch 50 results
            "media_filter": "gif",
        }
        response = await client.get(TENOR_API_URL, params=params)
        data = response.json()
        
        # Select a random GIF from the results
        random_gif = random.choice(data["results"])
        return random_gif["media_formats"]["gif"]["url"]

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    gif_url = await get_cat_gif_url()
    return templates.TemplateResponse("index.html", {"request": request, "url": gif_url})
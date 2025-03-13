from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import json
import random
import uvicorn
import os

app = FastAPI()

# Mount static files (for frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Constants for file paths
STORIES_FILE = "stories/stories.json"
JOKES_FILE = "jokes.json"
TRIVIA_FILE = "trivia.json"
FACTS_FILE = "facts.json"

# Function to load JSON files safely
def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Load data once at startup
stories = load_json_file(STORIES_FILE)
jokes = load_json_file(JOKES_FILE)
trivia = load_json_file(TRIVIA_FILE)
facts = load_json_file(FACTS_FILE)

# Helper functions to get random items
def get_random_item(data, category):
    return random.choice(data) if data else {"error": f"No {category} available"}

@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")

@app.get("/story")
def story():
    return {"story": get_random_item(stories, "stories")}

@app.get("/joke")
def joke():
    return {"joke": get_random_item(jokes, "jokes")}

@app.get("/fact")
def fact():
    return {"fact": get_random_item(facts, "facts")}

@app.get("/trivia")
def trivia_question():
    return {"trivia": get_random_item(trivia, "trivia")}

# Chatbot response endpoint
@app.get("/chat/{user_id}/{message}")
async def chat(user_id: int, message: str):
    message = message.lower()

    if "joke" in message:
        return JSONResponse({"response": get_random_item(jokes, "jokes")})
    elif "fact" in message:
        return JSONResponse({"response": get_random_item(facts, "facts")})
    elif "trivia" in message:
        return JSONResponse({"response": get_random_item(trivia, "trivia")})
    elif "story" in message:
        return JSONResponse({"response": get_random_item(stories, "stories")})
    else:
        return JSONResponse({"response": "I don't understand. Try asking for a joke, fact, trivia, or story!"})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

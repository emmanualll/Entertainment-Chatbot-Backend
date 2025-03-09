from fastapi import FastAPI
import json
import random
import os

app = FastAPI()

# Load stories at startup
STORIES_FILE = "stories/stories.json"

if os.path.exists(STORIES_FILE):
    with open(STORIES_FILE, "r", encoding="utf-8") as f:
        stories = json.load(f)
else:
    stories = []

# Load jokes, trivia, and facts
def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

jokes = load_json_file("jokes.json")
trivia = load_json_file("trivia.json")
facts = load_json_file("facts.json")


def get_random_story():
    """Returns a random story from the loaded stories."""
    return random.choice(stories) if stories else {"error": "No stories available"}

def get_random_joke():
    """Returns a random joke."""
    return random.choice(jokes) if jokes else {"error": "No jokes available"}

def get_random_fact():
    """Returns a random fact."""
    return random.choice(facts) if facts else {"error": "No facts available"}

def get_random_trivia():
    """Returns a random trivia question."""
    return random.choice(trivia) if trivia else {"error": "No trivia available"}

@app.get("/story")
def story():
    return {"story": get_random_story()}

@app.get("/joke")
def joke():
    return {"joke": get_random_joke()}

@app.get("/fact")
def fact():
    return {"fact": get_random_fact()}

@app.get("/trivia")
def trivia_question():
    return {"trivia": get_random_trivia()}

@app.get("/")
def home():
    return {"message": "Welcome to the Entertainment Chatbot API!"}

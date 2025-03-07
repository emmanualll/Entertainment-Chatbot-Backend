from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running on GitHub Codespaces!"}

@app.get("/play-rps/{user_choice}")
def play_rps(user_choice: str):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    if user_choice not in choices:
        return {"error": "Invalid choice! Choose rock, paper, or scissors."}

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    return {
        "your_choice": user_choice,
        "bot_choice": bot_choice,
        "result": result
    }
# 🎮 Guess the Number
@app.get("/guess-number/{user_guess}")
def guess_number(user_guess: int):
    number = random.randint(1, 10)

    if user_guess == number:
        result = "You guessed it right!"
    else:
        result = f"Wrong guess! The correct number was {number}."

    return {
        "your_guess": user_guess,
        "correct_number": number,
        "result": result
    }

# 🎮 Coin Toss
@app.get("/coin-toss")
def coin_toss():
    outcome = random.choice(["Heads", "Tails"])
    return {"coin_result": outcome}

# 🎮 Word Scramble
words = ["python", "fastapi", "developer", "hackathon", "backend"]

@app.get("/scramble-word")
def scramble_word():
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    return {"scrambled_word": scrambled, "original_word": word}

# Sample story prompts and continuations
story_prompts = {
    "adventure": "You find an ancient map leading to a hidden treasure deep in the jungle...",
    "sci-fi": "The spaceship trembled as you activated the hyperdrive, warping into an unknown galaxy...",
    "mystery": "A strange letter appears at your doorstep, sealed with an ancient symbol...",
    "fantasy": "As you touch the glowing sword, you feel a surge of magical energy course through you...",
}

@app.get("/start-story/{genre}")
def start_story(genre: str):
    if genre.lower() not in story_prompts:
        return {"error": "Invalid genre! Choose adventure, sci-fi, mystery, or fantasy."}

    return {"genre": genre, "story": story_prompts[genre.lower()]}

@app.get("/continue-story/{genre}")
def continue_story(genre: str):
    story_continuations = {
        "adventure": [
            "Following the map, you uncover a hidden cave filled with golden artifacts.",
            "Suddenly, a group of explorers appear, claiming they have been searching for the treasure for years.",
            "A trapdoor opens beneath your feet, leading to an underground tunnel!"
        ],
        "sci-fi": [
            "The control panel flickers, signaling an approaching alien fleet.",
            "You receive a cryptic transmission from an unknown source, warning you to turn back.",
            "An asteroid field appears out of nowhere, forcing you to make a quick decision!"
        ],
        "mystery": [
            "You open the letter and find an old photograph of a place you've never seen before.",
            "A shadowy figure watches you from across the street, then disappears into the night.",
            "A hidden compartment in your bookshelf clicks open, revealing a dusty diary."
        ],
        "fantasy": [
            "A dragon descends from the sky, its eyes glowing with wisdom.",
            "The sword in your hands whispers ancient words, guiding you towards your destiny.",
            "A portal opens before you, revealing a kingdom lost to time."
        ],
    }

    if genre.lower() not in story_continuations:
        return {"error": "Invalid genre! Choose adventure, sci-fi, mystery, or fantasy."}

    return {"genre": genre, "story": random.choice(story_continuations[genre.lower()])}
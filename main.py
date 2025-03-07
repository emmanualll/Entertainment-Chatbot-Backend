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

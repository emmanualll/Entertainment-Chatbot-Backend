from fastapi import FastAPI
from games import (
    play_rock_paper_scissors, start_guess_number, guess_number,
    start_tic_tac_toe, play_tic_tac_toe,
    start_word_scramble, guess_word_scramble
)

app = FastAPI()

@app.get("/chat/{user_id}/{user_message}")
def chatbot_response(user_id: str, user_message: str):
    user_message = user_message.lower()

    # Rock-Paper-Scissors
    if user_message in ["rock", "paper", "scissors"]:
        return {"response": play_rock_paper_scissors(user_id, user_message)}

    # Guess the Number
    if "start guess the number" in user_message:
        return {"response": start_guess_number(user_id)}
    if user_message.isdigit():
        return {"response": guess_number(user_id, user_message)}

    # Tic-Tac-Toe
    if "start tic-tac-toe" in user_message:
        return {"response": start_tic_tac_toe(user_id)}
    if user_message.isdigit():
        return {"response": play_tic_tac_toe(user_id, user_message)}

    # Word Scramble
    if "start word scramble" in user_message:
        return {"response": start_word_scramble(user_id)}
    if len(user_message) > 2:
        return {"response": guess_word_scramble(user_id, user_message)}

    return {"response": "I don't understand. Try asking me to play a game!"}

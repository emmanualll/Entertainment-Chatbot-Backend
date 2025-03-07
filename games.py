import random
import typing from Dict

# ================== Rock-Paper-Scissors ==================
def play_rock_paper_scissors(user_id, user_choice):
    """Handles Rock-Paper-Scissors game logic."""
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    if user_choice not in choices:
        return "Please choose rock, paper, or scissors!"

    if user_choice == bot_choice:
        update_score(user_id, "tie")
        result = "It's a tie!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        update_score(user_id, "win")
        result = "You win!"
    else:
        update_score(user_id, "loss")
        result = "I win!"

    scores = get_scores(user_id)
    return f"You chose {user_choice}, I chose {bot_choice}. {result} | Wins: {scores['wins']}, Losses: {scores['losses']}, Ties: {scores['ties']}"

# ================== Guess the Number ==================
active_games = {}  # Stores active number-guessing games

def start_guess_number(user_id):
    """Starts a new 'Guess the Number' game."""
    number = random.randint(1, 10)  # Bot picks a number
    active_games[user_id] = number
    return "I've picked a number between 1 and 10. Try to guess it!"

def guess_number(user_id, guess):
    """Handles user guesses."""
    if user_id not in active_games:
        return "Start a new game first by saying 'start guess the number'."

    try:
        guess = int(guess)
    except ValueError:
        return "Please enter a valid number between 1 and 10."

    number = active_games[user_id]
    
    if guess < number:
        return "Too low! Try again."
    elif guess > number:
        return "Too high! Try again."
    else:
        del active_games[user_id]  # End game
        update_score(user_id, "win")
        return f"Correct! You guessed the number. Your new score: {get_scores(user_id)}"

# ================== Tic-Tac-Toe ==================
ttt_boards = {}  # Stores Tic-Tac-Toe boards for active users

def start_tic_tac_toe(user_id):
    """Starts a new Tic-Tac-Toe game."""
    board = [" "]*9  # Empty board
    ttt_boards[user_id] = board
    return "Tic-Tac-Toe started! You play as 'X'. Choose a position (1-9)."

def play_tic_tac_toe(user_id, position):
    """Handles Tic-Tac-Toe game moves."""
    if user_id not in ttt_boards:
        return "Start a game first by saying 'start tic-tac-toe'."

    try:
        position = int(position) - 1  # Convert to 0-based index
        if position < 0 or position > 8 or ttt_boards[user_id][position] != " ":
            return "Invalid move! Pick an empty spot (1-9)."
    except ValueError:
        return "Enter a valid number between 1 and 9."

    # Player move
    board = ttt_boards[user_id]
    board[position] = "X"

    # Check if player won
    if check_tic_tac_toe_winner(board, "X"):
        del ttt_boards[user_id]
        update_score(user_id, "win")
        return "You win! Tic-Tac-Toe over."

    # Bot move (random)
    empty_positions = [i for i, spot in enumerate(board) if spot == " "]
    if empty_positions:
        bot_move = random.choice(empty_positions)
        board[bot_move] = "O"

        # Check if bot won
        if check_tic_tac_toe_winner(board, "O"):
            del ttt_boards[user_id]
            update_score(user_id, "loss")
            return "I win! Tic-Tac-Toe over."

    return f"Your move:\n{format_board(board)}\nNow it's my turn!"

def check_tic_tac_toe_winner(board, player):
    """Checks if a player has won."""
    win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_positions)

def format_board(board):
    """Formats Tic-Tac-Toe board for display."""
    return f"{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | {board[8]}"

# ================== Word Scramble ==================
words = ["python", "fastapi", "database", "backend", "frontend"]
scrambled_games = {}

def start_word_scramble(user_id):
    """Starts a new Word Scramble game."""
    word = random.choice(words)
    scrambled_word = "".join(random.sample(word, len(word)))  # Shuffle letters
    scrambled_games[user_id] = word
    return f"Unscramble this word: {scrambled_word}"

def guess_word_scramble(user_id, guess):
    """Checks if the user guessed the scrambled word correctly."""
    if user_id not in scrambled_games:
        return "Start a new game first by saying 'start word scramble'."

    correct_word = scrambled_games[user_id]
    if guess.lower() == correct_word:
        del scrambled_games[user_id]
        update_score(user_id, "win")
        return f"Correct! The word was '{correct_word}'. Your new score: {get_scores(user_id)}"
    else:
        return "Wrong! Try again."


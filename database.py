import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("game_scores.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table for storing user scores
cursor.execute("""
CREATE TABLE IF NOT EXISTS scores (
    user_id TEXT PRIMARY KEY,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    ties INTEGER DEFAULT 0
)
""")
conn.commit()

def get_scores(user_id):
    """Retrieve scores for a specific user."""
    cursor.execute("SELECT wins, losses, ties FROM scores WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    
    if result:
        return {"wins": result[0], "losses": result[1], "ties": result[2]}
    else:
        # If user is new, insert them into the database
        cursor.execute("INSERT INTO scores (user_id, wins, losses, ties) VALUES (?, 0, 0, 0)", (user_id,))
        conn.commit()
        return {"wins": 0, "losses": 0, "ties": 0}

def update_score(user_id, result):
    """Update the user's score based on the game result."""
    scores = get_scores(user_id)

    if result == "win":
        scores["wins"] += 1
    elif result == "loss":
        scores["losses"] += 1
    elif result == "tie":
        scores["ties"] += 1

    cursor.execute("""
        UPDATE scores 
        SET wins = ?, losses = ?, ties = ? 
        WHERE user_id = ?
    """, (scores["wins"], scores["losses"], scores["ties"], user_id))
    
    conn.commit()

def reset_scores(user_id):
    """Reset a user's scores to zero."""
    cursor.execute("UPDATE scores SET wins = 0, losses = 0, ties = 0 WHERE user_id = ?", (user_id,))
    conn.commit()
    return "Scores have been reset!"

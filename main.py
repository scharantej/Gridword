
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import random
import json

# Initialize the Flask application
app = Flask(__name__)

# Route to generate a new game grid
@app.route('/generate-grid', methods=['GET'])
def generate_grid():
    # Create a 4x4 grid of letter tiles
    grid = [['' for _ in range(4)] for _ in range(4)]

    # Populate the grid with random letters
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(4):
        for j in range(4):
            grid[i][j] = random.choice(alphabet)

    # Convert the grid to a JSON object and return it
    grid_json = json.dumps(grid)
    return grid_json

# Route to check if a word is present in the grid
@app.route('/check-word', methods=['POST'])
def check_word():
    # Get the word from the request
    word = request.get_json()['word']

    # Convert the grid to a 1D array
    grid = sum(grid, [])

    # Check if the word is present in the grid
    if word in grid:
        return jsonify({'found': True})
    else:
        return jsonify({'found': False})

# Route to calculate the score for a word
@app.route('/get-score', methods=['POST'])
def get_score():
    # Get the word from the request
    word = request.get_json()['word']

    # Calculate the score
    score = len(word) * 10

    # Return the score
    return jsonify({'score': score})

# Route to save the game progress
@app.route('/save-game', methods=['POST'])
def save_game():
    # Get the game state from the request
    game_state = request.get_json()['game_state']

    # Save the game state to a database

    # Return a success message
    return jsonify({'success': True})

# Route to load the saved game
@app.route('/load-game', methods=['POST'])
def load_game():
    # Get the user's ID from the request
    user_id = request.get_json()['user_id']

    # Load the saved game state from the database

    # Return the game state
    return jsonify({'game_state': game_state})

# Main function to start the Flask application
if __name__ == '__main__':
    app.run(debug=True)

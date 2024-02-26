## Flask Application Design for a Word Search Game

### Overview
- We're designing a Flask application that presents a 4x4 grid-based word search game.
- The game will display a grid with letter tiles, and users can drag and drop these tiles to form words.
- Users will score points by finding words, and the game ends when all the words are found or a time limit expires.

### HTML Files

**1. index.html**
- This is the main HTML page that loads when the user opens the game.
- It contains the grid, a scoring section, a timer, and a list of instructions.

**2. drag_and_drop.js**
- This JavaScript file handles the drag-and-drop functionality of the letter tiles.
- It tracks the user's mouse movements and updates the position of the tiles accordingly.

**3. word_search.css**
- This CSS file contains the styling for the game, including the layout of the grid, the font of the letters, and the colors used.

### Routes

**1. /generate-grid**
- This route is responsible for generating a new 4x4 grid of letter tiles.
- It accepts a GET request and returns a JSON object containing the grid data, including the positions and letters on the tiles.

**2. /check-word**
- This route checks if a given word is present in the grid.
- It accepts a POST request with the word as a parameter and returns a JSON object indicating whether the word was found.

**3. /get-score**
- This route calculates the score for a given word.
- It accepts a POST request with the word as a parameter and returns a JSON object containing the score.

**4. /save-game**
- This route allows users to save their game progress.
- It accepts a POST request with the game state as a parameter and stores it in a database.

**5. /load-game**
- This route allows users to load a saved game.
- It accepts a POST request with the user's ID as a parameter and returns a JSON object containing the saved game state.
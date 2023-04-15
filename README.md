# SuperMinesweeper
Implemented the two-dimensional minesweeper game with Python and extended its function to n-dimensional boards in which each cell has 3n-1 neighbors
## Gameplay

To play, run `server.py`.

All gameboard are representated as a dictionary, containing: 
dimension of the board, 
an N-dimensional array representing the game board with position of bombs, 
an N-dimensional array to keep track of whether a position is revealed,
and a string indicating the game state(ongoing, victory or defeat)


## Game Interface

Two-dimensional game:

<img width="803" alt="Screen Shot 2023-04-15 at 10 56 15" src="https://user-images.githubusercontent.com/105997889/232232446-0c1b132c-7d19-4dc0-b0bb-e3eedfd5de99.png">

N-dimensional game: 

<img width="811" alt="Screen Shot 2023-04-15 at 10 40 25" src="https://user-images.githubusercontent.com/105997889/232232296-1880b169-5f94-430c-a138-e474fea9fb57.png">

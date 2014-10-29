My-Chess-Game
=============

My first program. A rudimentary chess game.

I began this program immediately following my initial completion of a couple of python tutorials.
This code is likely to be wholly unpythonic.

I'm obviously not attempting any sort of AI in this chess game. This is intended to be a 2 player game
in which players can move pieces using standard Algebraic notation (E2 to E4 for advancing the king's pawn
by 2). It, of course, when fully implemented, will only allow valid chess moves and will end the game given
checkmate or draw conditions. I would like to eventually implement an ASCII board (I have a sample in the comments
of the board file at the very bottom) which would load before each move.

For the time being I have several files which use objects and functions from all the files without
the proper import statements. I have tried to group the files with all the piece-specific functions and objects
in one document, the board-specific ones in another, turn order in another, and a main file which will call
all the relevant functions to run them.

Things I'd like to add when fully functional:

A save/load game feature.
Saving a log of the moves of a game.



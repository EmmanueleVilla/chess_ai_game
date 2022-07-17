### Moves
* Add en passant capture
* Add castling
* Add + or # at the end of the move based on the enemy king state
* Remove invalid moves (where owned king is in check afterwards)
* Add coordinate(s) to ambiguos moves
### Tests
* Unit tests that re-play the saved games and fails if a move is illegal
### AI game
* Set number of games as arg
* Accept N AIs as args and start tournament
* Draw after 50 turns without captures or pawn moving
* Draw after 250 turns
### Log
Save match.log with the moves with additional info if a move was invalid
### Refactor
* Add types to methods
* Choose and follow a standard for the command line arguments 

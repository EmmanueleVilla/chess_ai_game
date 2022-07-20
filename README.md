# Chess AI Game

Chess AI Game is an artificial intelligence game written in python where two external artificial intelligence programs
play chess against each other.

It's still a work in progress, and I'm learning python while doing it, so it may suck :)

Yes, I know there are already lots of programs like this and official chess AI tournaments and stuff, this is just an
exercise

It is composed by a simple UI made with pygame

## Usage

To play, you need to call

```
python3 main.py "command to execute the first AI" "command to execute the second AI"
```

In the AI folder there's a simple AI that plays a random move, giving priority to moves that capture, check and
checkmate the opponent. Given the format above, you can start the game by executing:

```
python3 main.py "python3 AI/stupid_ai.py" "python3 AI/stupid_ai.py"
```

In the console you can see the games id and the results of 10 games:

```
2022_07_19_17_52_06_129423
Game 0: 0.5-0.5 (50 Rule)
Game 1: 0.5-0.5 (50 Rule)
Game 2: 0-1 (Checkmate)
Game 3: 1-0 (Checkmate)
Game 4: 0.5-0.5 (Repetition)
Game 5: 0.5-0.5 (Repetition)
Game 6: 0.5-0.5 (Stalemate)
Game 7: 0.5-0.5 (Repetition)
Game 8: 0.5-0.5 (Repetition)
Game 9: 0.5-0.5 (Repetition)
Results: 5.0-5.0
```

An explanation of why the match ended is explicited at the end of each game. The explanation can be Checkmate,
Stalemate, 50 Rule or Repetition. The game may also end when it reaches the 1000th turn, but it should be impossible :P

You can see an example of games played [on youtube](https://youtu.be/hnC_k2zBkHU)

## Logs

During play, a folder named logs/{games_id} will be created in the root of the project. This folder contains a log file (with the same output as the console) and 10
sub-folders (one for each game played), containing 3 files:

* an.txt: the log of the game using the [Algebraic Notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)).

Example:

```
1. d4 Nf6
2. e3 Ng4
3. Qxg4 a6
4. Qxd7+ Nxd7
5. Bxa6 bxa6
6. Kf1 Ra7
7. h3 Nc5
8. dxc5 Qd1#
0-1
```

* board.txt: the log of the game composed by the print of all the boards state. This is a colored log, so you'll want to
  cat the file in a terminal
* message.txt: this is the file used for communication between the main game and the AI

## Communication

When the game needs to request a move from a player, it creates a txt file containing the board state, composed like
this:

```
board_size
{board_size}
turn_number
{turn_number}
turn_color
{turn_color}
pieces
{first_piece}
{second_piece}
...
moves
{first_move}
{second_move}
...
```

For example:

```
board_size
8
turn_number
101
turn_color
Color.WHITE
pieces
KW: b1
KB: d1
moves
Kb2
Ka1
Ka2
```

The AI program will receive the path of this file as the first and unique command line arg. It must open the file, parse
it and respond using a console log, printing the code of the move to be executed and then interrupt itself with an exit
call.

If the response is not included in the move list sent by the program, that player will skip the turn and an "Invalid
Move"
step will be printed in the logs

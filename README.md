# Chess AI Game

This is an experiment of a chess game with external configurable artificial intelligence.

It's a work in progress and I'm just learning python, so it sucks :)

## Description

Chess AI Game is a game where you develop your own artificial intelligence to play chess and attach it to the main
executable to play.

Yes, I know there are already lots of programs like this and official AI tournaments and stuff, this is just an exercise

## Usage

To play, you need to call

```
python3 main.py "command to execute the first AI" "command to execute the second AI" "command to execute the third AI" ...
```

At the moment, only two AI are supported: for example, to use the default AI call:

```
python3 main.py "python3 AI/stupid_ai.py" "python3 AI/stupid_ai.py"
```

The AI executable will receive the path of a file containing the state of the board and the possible moves via args, it
must print to the console the move and then exit(0).

Output example:

```
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

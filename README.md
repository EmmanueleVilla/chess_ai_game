# Chess AI Game

This is an experiment of a chess game with external configurable artificial intelligence.

It's a work in progress and I'm just learning python, so it sucks :)

## Description

Chess AI Game is a game where you develop your own artificial intelligence to play chess and attach it to the main executable to play.

Yes, I know there are already lots of programs like this and official AI tournaments and stuff, this is just an exercise

## Usage

To play, you'll just need to call

```
python3 main.py "command to execute the first AI" "command to execute the second AI"
```

For example, to use the default AI:

```
python3 main.py "python3 AI/stupid_ai.py" "python3 AI/stupid_ai.py"
```

The output will be the board:

![Board](/images/preview.png "The board")

The AI executable will receive the state of the board via args and must print to the console the move. The communication interface is yet to be determined

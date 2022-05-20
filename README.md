# An Adventure

A console game which finds the shortest path in a maze provided by the player. Beware: there are monsters waiting for you along the way!

## Requirements:

- [Python](https://www.python.org/downloads/)
- [d20](https://pypi.org/project/d20/)
- A text file with a maze; there are example files in the `maps` folder.

## How does the maze text file need to look like?

The file contains the maze only. The maze consists of `X` and `-`, where `-` are the way, and `X` are the obstacles (user cannot move on them). The starting point must be (0, 1). Should you have any doubts, check out example mazes in the `maps` folder.

## How to play?

Download the [game files](https://git.syberry.com/syberry-academy/syberry-academy-season-8/crew-b108-project/-/archive/dev/crew-b108-project-dev.zip) from the `dev` branch. Unpack them if zipped, open command line in the root folder, and type `python .\Game.py [path_to_file_with_maze]`. The game will now start.

Another example: 
`python .\Game.py maps/case-1.txt`

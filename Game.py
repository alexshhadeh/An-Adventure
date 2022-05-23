import sys

from src.Maze import Maze
from src.ShortestPath import ShortestPath
from src.CombatSystem import CombatSystem

if __name__ == '__main__':
    maze1 = Maze(sys.argv[1])
    maze_path = ShortestPath(maze1.maze).findShortestPath()

    cs_user = CombatSystem()

    maze1.adventure(maze_path, cs_user)
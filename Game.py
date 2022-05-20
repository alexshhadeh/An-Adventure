from src.Maze import Maze
from src.ShortestPath import ShortestPath
from src.CombatSystem import CombatSystem

if __name__ == '__main__':
    maze1 = Maze("maps/case-1.txt")
    maze_path = ShortestPath(maze1.maze).findShortestPath()

    cs_user = CombatSystem()

    maze1.adventure(maze_path, cs_user)
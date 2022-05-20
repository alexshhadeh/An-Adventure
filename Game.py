from src.Maze import Maze
from src.ShortestPath import ShortestPath
from src.CombatSystem import CombatSystem

if __name__ == '__main__':
    maze1 = Maze("maps/case-3.txt")

    cs_user = CombatSystem()
    cs_user.character_select()

    maze_path = ShortestPath(maze1.maze).findShortestPath()

    maze1.adventure(maze_path, cs_user)
from src.Maze import Maze
from src.ShortestPath import ShortestPath

if __name__ == '__main__':
    # maze6 = Maze("../maps/case-6.txt")
    # maze6.print_maze()

    maze1 = Maze("maps/case-1.txt")
    maze1.print_maze()

    maze_starting_point = {'x': 1, 'y': 0}
    maze_path = ShortestPath(maze1.maze, maze_starting_point)
    print(maze_path.findShortestPath())

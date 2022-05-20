import os
import time


def handle_error(error, tile=""):
    os.system('cls')

    if "empty_file":
        print("File is empty.")
    if "maze_one_line":
        print("Maze cannot be one line.")
    if "maze_not_rectangle":
        print('Maze must have rectangular shape.')
    if "unknown_tile":
        print('find foreign tile : ' + tile + ".")
    if "starting_tile_not_found":
        print('Starting tile must be (1,0).')
    if _:
        print("Error occurred.")

    exit(1)


def check_tiles(maze):
    if maze[1][0] != '-':
        handle_error("starting_tile_not_found")
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] != 'x' and maze[i][j] != '-':
                handle_error("unknown_tile", maze[i][j])


class Maze:

    def __init__(self, path):
        if os.stat(path).st_size == 0:
            handle_error("empty_file")

        file = open(path, 'r')
        maze = []
        self.is_path_found = False

        is_first_line = True
        line_length = 0
        line_row = 0
        for line in file:
            if is_first_line:
                line_length = len(line)
                is_first_line = False
            elif len(line) > line_length:
                handle_error("maze_not_rectangle")
            maze.append([])
            for j in range(len(line)):
                if line[j] == '\n':
                    break
                maze[line_row].append(line[j])
            line_row = line_row + 1

        if line_row == 1:
            handle_error("maze_one_line")
        check_tiles(maze)
        self.maze = maze

    def print_maze(self):
        str_out = ""
        for line in self.maze:
            for tile in line:
                str_out = str_out + tile + " "
            str_out = str_out + "\n"

        os.system("cls")

        if self.is_path_found:
            print("Here is a shortest path\n")
        else:
            print("The new maze\n")

        print(str_out)

    def adventure(self, short_path):
        encounters = 0
        # short_path = [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2},
        #               {'x': 3, 'y': 2}, {'x': 3, 'y': 3}, {'x': 3, 'y': 4}]
        for tile in short_path:
            for coord, val in tile.items():
                self.next_tile(tile)

    def __next_tile(self, tile):
        self.maze[tile[0]][tile[1]] = "o"
        self.__print_maze()
        time.sleep(0.5)

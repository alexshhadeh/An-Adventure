import os
import random
import time
from src.CombatSystem import CombatSystem


def handle_error(error, tile=""):
    os.system('cls')

    if error == "empty_file":
        print("File is empty.")
    elif error == "maze_one_line":
        print("Maze cannot be one line.")
    elif error == "maze_not_rectangle":
        print('Maze must have rectangular shape.')
    elif error == "unknown_tile":
        print('find foreign tile : ' + tile + ".")
    elif error == "starting_tile_not_found":
        print('Starting tile must be (1,0).')
    elif error == "no_exit":
        print('The maze has no exit.')
    else:
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
        self.__print_maze()

    def __print_maze(self, msg=""):
        str_out = ""
        for line in self.maze:
            for tile in line:
                str_out = str_out + tile + " "
            str_out = str_out + "\n"

        os.system("cls")
        if msg == "":
            if self.is_path_found:
                print("Here is the shortest path\n")
            else:
                print("The new maze\n")
        else:
            print(msg)

        print(str_out)
        time.sleep(1)

    def adventure(self, short_path, cs_user: CombatSystem):
        if len(short_path) == 1 or len(short_path) == 0:
            handle_error("no_exit")
        cs_user.character_select()
        self.is_path_found=True
        encounters_number = len(short_path) // 2
        if encounters_number == 0:
            encounters_number += 1
        encounter_tiles = []
        for encounter in range(encounters_number):
            encounter_tiles.append(random.choice(short_path))
        enc_i = 0
        for tile in short_path:
            for i in range(2):
                current_tile = []
                for k, v in tile.items():
                    current_tile.append(v)
            self.maze[current_tile[0]][current_tile[1]] = "o"
            os.system("cls")
            print("Going to: ({x},{y})".format(x=current_tile[0], y=current_tile[1]))
            time.sleep(1)
            self.__print_maze("You are at: ({x},{y})".format(x=current_tile[0], y=current_tile[1]))
            if tile == encounter_tiles[enc_i]:
                cs_user.generate_battle()
            time.sleep(1)
            if enc_i < encounters_number - 1:
                enc_i += 1

        print("Hooray, you have found the exit!")

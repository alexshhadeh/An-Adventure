rawMaze = [
    ['XXXXX'],
    ['---XX'],
    ['XX-XX'],
    ['XX---'],
    ['XX-XX']
]


class Maze:
    def __init__(self, rawMaze, startingPoint) -> None:
        self.maze = rawMaze
        for i, v in enumerate(self.maze):
            self.maze[i] = list(v[0])
        self.startingPoint = startingPoint
        self.branches = []
        self.createdNewBranch = False

    def findAllPaths(self):
        self.findPath([self.startingPoint])
        while self.createdNewBranch:
            self.createdNewBranch = False
            for path in self.branches:
                self.findPath(path)

        return self.branches

    def findShortestPath(self):
        self.findAllPaths()
        shortest = self.branches[0]
        for path in self.branches:
            if len(path) < len(shortest):
                shortest = path
        return shortest

    def findPath(self, path):
        currentPoint = path[len(path)-1]
        foundPoints = self.filterPoints(self.findPoints(currentPoint), path)

        if len(foundPoints) > 1:
            for _, point in enumerate(foundPoints, 1):
                if self.isInMaze(point):
                    branch = list(path)
                    branch.append(point)
                    self.branches.append(branch)
                    self.createdNewBranch = True

        for point in foundPoints:
            if self.isInMaze(point):
                path.append(point)
                return self.findPath(path)
        return path

    """def findPath(maze, path):
		currentPoint=path[len(path)-1]
		foundPoints=filterPoints(findPoints(maze, currentPoint), path)
		for point in foundPoints:
			if isInMaze(point, maze):
				path.append(point)
				return findPath(maze, path)
		return path"""

    def isInMaze(self, point):
        if point['x'] < 0 or point['y'] < 0:
            return False
        elif point['x'] > len(self.maze)-1 or point['y'] > len(self.maze)-1:
            return False
        else:
            return True

    def filterPoints(self, points, path):
        filteredPoints = [point for point in points if point not in path]
        return filteredPoints

    def findPoints(self, startingPoint):
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        foundPoints = []
        for direction in directions:
            checkedPoint = {
                'x': startingPoint['x']+direction[0],
                'y': startingPoint['y']+direction[1]
            }
            try:
                pointOnMap = self.maze[checkedPoint['x']][checkedPoint['y']]
                if self.pointIsAccessible(pointOnMap):
                    foundPoints.append(checkedPoint)
            except IndexError:
                foundPoints.append(checkedPoint)
        return foundPoints

    def pointIsAccessible(self, pointOnMap):
        if(pointOnMap == "-"):
            return True
        return False


mazeStartingPoint = {'x': 1, 'y': 0}
maze = Maze(rawMaze, mazeStartingPoint)
print(maze.findShortestPath())
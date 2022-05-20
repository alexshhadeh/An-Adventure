class ShortestPath:

    def __init__(self, rawMaze, startingPoint={'x': 1, 'y': 0}):
        self.maze = rawMaze
        # for (i, v) in enumerate(self.maze):
        #     self.maze[i] = list(v[0])
        self.maze = rawMaze
        self.startingPoint = startingPoint
        self.branches = []
        self.createdNewBranch = False

    def findAllPaths(self):
        onePath = self.findPath([self.startingPoint])
        while self.createdNewBranch:
            self.createdNewBranch = False
            for path in self.branches:
                self.findPath(path)
        if len(self.branches) == 0:
            self.branches.append(onePath)
        for path in self.branches:
            if self.isThereAnExit(path[len(path) - 1]) is False:
                self.branches.remove(path)
        return self.branches

    def findShortestPath(self):
        self.findAllPaths()
        if len(self.branches) == 0:
            return []
        shortest = self.branches[0]
        for path in self.branches:
            if len(path) < len(shortest):
                shortest = path
        return shortest

    def findPath(self, path):
        currentPoint = path[len(path) - 1]
        foundPoints = self.filterPoints(self.findPoints(currentPoint), path)

        for point in foundPoints:
            if self.isInMaze(point) is False:
                return path

        if len(foundPoints) > 1:
            for (_, point) in enumerate(foundPoints, 1):
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

    def isThereAnExit(self, point):
        for point in self.findAllPossiblePoints(point):
            if self.isInMaze(point) is False:
                return True
        return False

    def isInMaze(self, point):
        if (point['x'] < 0 or point['y'] < 0 or
                point['x'] > len(self.maze) - 1 or
                point['y'] > len(self.maze) - 1):
            return False
        else:
            return True

    def filterPoints(self, points, path):
        filteredPoints = [point for point in points if point
                          not in path]
        return filteredPoints

    def findAllPossiblePoints(self, startingPoint):
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        foundPoints = []
        for direction in directions:
            checkedPoint = {'x': startingPoint['x'] + direction[0],
                            'y': startingPoint['y'] + direction[1]}
            foundPoints.append(checkedPoint)
        return foundPoints

    def findPoints(self, startingPoint):
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        foundPoints = []
        for direction in directions:
            checkedPoint = {'x': startingPoint['x'] + direction[0],
                            'y': startingPoint['y'] + direction[1]}
            try:
                pointOnMap = self.maze[checkedPoint['x']][checkedPoint['y']]
                if self.pointIsAccessible(pointOnMap):
                    foundPoints.append(checkedPoint)
                elif (checkedPoint['y'] == -1 and
                      startingPoint != {'x': 1, 'y': 0}):
                    foundPoints.append(checkedPoint)
            except IndexError:
                foundPoints.append(checkedPoint)
        return foundPoints

    def pointIsAccessible(self, pointOnMap):
        if pointOnMap == '-':
            return True
        return False

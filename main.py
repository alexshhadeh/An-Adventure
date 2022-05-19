maze=[
['XXXXX'],
['---XX'],
['XX-XX'],
['XX---'],
['XX-XX']
]

for i, v in enumerate(maze):
	#print(x)
	maze[i]=list(v[0])

def displayShortestPath(maze, startingPoint):
	shortestPath=findShortestPath(paths)
	mazeWithPath=plotPathOnMaze(shortestPath, maze)
	print(mazeWithPath)

def plotPathOnMaze(path, maze):
	return mazeWithPath

def findShortestPath(paths):
	mini=paths[0]
	for path in paths:
		if len(path)<len(mini):
			mini=path
	return mini

def addPoint(path, point):
	path.append(point)
	return path

#one version of the algorithm: currently finds only one way out
def findPath(maze, path):
	currentPoint=path[len(path)-1]
	foundPoints=filterPoints(findPoints(maze, currentPoint), path)
	#print(foundPoints)
	for point in foundPoints:
		#print(point)
		if isInMaze(point, maze):
			path.append(point)
			return findPath(maze, path)
	return path

#second version of the algorithm: finds all of the coordinates but unsorted
def findPaths(maze, path):
	paths=[]
	currentPoint=path[len(path)-1]
	foundPoints=filterPoints(findPoints(maze, currentPoint), path)
	if len(foundPoints)==1:
		if isInMaze(foundPoints[0], maze):
			findPaths(maze, addPoint(path, foundPoints[0]))
	if len(foundPoints)==2:
		if isInMaze(foundPoints[0], maze):
			findPaths(maze, addPoint(path, foundPoints[0]))
		if isInMaze(foundPoints[1], maze):
			findPaths(maze, addPoint(path, foundPoints[1]))
	if len(foundPoints)==3:
		if isInMaze(foundPoints[0], maze):
			findPaths(maze, addPoint(path, foundPoints[0]))
		if isInMaze(foundPoints[1], maze):
			findPaths(maze, addPoint(path, foundPoints[1]))
		if isInMaze(foundPoints[2], maze):
			findPaths(maze, addPoint(path, foundPoints[2]))
	return path


def isInMaze(point, maze):
	try:
		maze[point['x']][point['y']]
	except IndexError:
		return False
	return True

def filterPoints(points, path):
	filteredPoints=[point for point in points if point not in path]
	return filteredPoints

def findPoints(maze, startingPoint):
	"""print("Starting point:")
	print(startingPoint)"""
	directions=[[0, -1], [0, 1], [-1, 0], [1, 0]]
	foundPoints=[]
	for direction in directions:
		checkedPoint={
		'x':startingPoint['x']+direction[0],
		'y':startingPoint['y']+direction[1]
		}
		try:
			pointOnMap=maze[checkedPoint['x']][checkedPoint['y']]
			if pointIsAccessible(pointOnMap):
				foundPoints.append(checkedPoint)
		except IndexError:
			foundPoints.append(checkedPoint)

	return foundPoints

def pointIsAccessible(pointOnMap):
	if(pointOnMap=="-"):
		return True
	return False

#finds one path
print(findPath(maze, [{'x':1, 'y':0}]))

#finds all paths' coordinates
print(findPaths(maze, [{'x':1, 'y':0}]))

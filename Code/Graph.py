import numpy as np


class Graph:
    # Initialize graph
    def __init__(self, graphDict=None, oriented=True):
        self.graphDict = graphDict or {}
        self.oriented = oriented
        if not oriented:
            self.convertToUndirected()
    # Convert a directed graph to an undirected graph

    def convertToUndirected(self):
        for a in list(self.graphDict.keys()):
            for (b, dist) in self.graphDict[a].items():
                self.graphDict.setdefault(b, {})[a] = dist

    # Add a connection between node A and B with a given weight,
    # if the graph is undirected, an additional connection from node B to node A is added
    def connect(self, A, B, distance=1):
        self.graphDict.setdefault(A, {})[B] = distance
        if not self.oriented:
            self.graphDict.setdefault(B, {})[A] = distance

    # Get adjacent nodes
    def get(self, a, b=None):
        connections = self.graphDict.setdefault(a, {})
        if b is None:
            return connections
        else:
            return connections.get(b, float('inf'))

    # Return a list of nodes
    def nodes(self):
        s1 = set([k for k in self.graphDict.keys()])
        s2 = set([k2 for v in self.graphDict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

    # Remove a node, i.e., a zone from the graph
    def remove(self, zoneList, zoneName):
        for i in range(len(zoneList)):
            if (self.graphDict[zoneList[i].name].get(zoneName) != None):
                self.graphDict[zoneList[i].name].pop(zoneName)
        self.graphDict.pop(zoneName)


class Node:
    # Create an instance of Node
    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        # Distance from initial node
        self.g = 0
        # Distance from target node
        self.h = 0
        # Total cost of distances
        self.f = 0
    # Compare nodes

    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes based on cost
    def __lt__(self, other):
        return self.f < other.f

    # Print nodes
    def __repr__(self):
        return '({0},{1})'.format(self.name, self.f)


class Zone:
    # Initialize the class
    def __init__(self, name: str):
        self.name = name
        self.pollutionFactors = createPollution()
        self.pollution = assignPollution(self.pollutionFactors)

# Generate a random pollution value between 0 and 100.
def createPollution():
    pollutionFactors = np.random.randint(100)

    return pollutionFactors

# Assign the pollution level
def assignPollution(pollutionFactors):
    if pollutionFactors <= 20:
        return 'veryLow'
    elif pollutionFactors <= 40:
        return 'low'
    elif pollutionFactors <= 60:
        return 'moderate'
    elif pollutionFactors <= 80:
        return 'high'
    else:
        return 'veryHigh'

# Calculates the actual cost of the path from node A to node B
def calculateRealCost(start, target):
    cost = (start + target) / 2
    
    return cost

# Estimates the cost of the path from node A to node B
def calculateHeuristic(start, target):
    heuristic = (start + target) / 2
    return heuristic

# Used to find the path from Zone A to Zone B in the graph
# Returns a vector that keeps all the heuristics for the zones in between A and B
def heuristicVector(zone:Zone, zoneList):
    heuristics = {}
    for i in range(len(zoneList)):
        heuristics[zoneList[i].name] = calculateHeuristic(zone.pollutionFactors, zoneList[i].pollutionFactors)
    return heuristics

# Checks whether an adjacent node has been added to the list of nodes yet to be examined (open)
def checkAddedNeighbor(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

# A* search
def AStarSearch(graph, heuristics, start: Zone, destination: Zone):
    
    open = []
    closed = []
    startNode = Node(start.name, None)
    golNode = Node(destination.name, None)
    open.append(startNode)

    while len(open) > 0:
        open.sort()
        currentNode = open.pop(0)
        closed.append(currentNode)

        if currentNode == golNode:
            path = []
            while currentNode != startNode:
                path.append(currentNode.name)
                currentNode = currentNode.parent
            path.append(startNode.name)
            return path[::-1]
        neighbor = graph.get(currentNode.name)
        for key, value in neighbor.items():
            neighbor = Node(key, currentNode)
            if (neighbor in closed):
                continue
            neighbor.g = (currentNode.g + graph.get(currentNode.name, neighbor.name)) / 2
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = (neighbor.g + neighbor.h) / 2
            if (checkAddedNeighbor(open, neighbor) == True):
                open.append(neighbor)
    return None

nodes = []
zone1_1 = Zone("1.1")
nodes.append(zone1_1)
zone1_2 = Zone("1.2")
nodes.append(zone1_2)
zone1_3 = Zone("1.3")
nodes.append(zone1_3)
zone2_1 = Zone("2.1")
nodes.append(zone2_1)
zone2_2 = Zone("2.2")
nodes.append(zone2_2)
zone3_1 = Zone("3.1")
nodes.append(zone3_1)
zone3_2 = Zone("3.2")
nodes.append(zone3_2)
zone4_1 = Zone("4.1")
nodes.append(zone4_1)
zone4_2 = Zone("4.2")
nodes.append(zone4_2)
zone4_3 = Zone("4.3")
nodes.append(zone4_3)


# Generates the graph
def generateGraph():

    graph = Graph()

    graph.connect(zone1_1.name, zone1_2.name, calculateRealCost(
        zone1_1.pollutionFactors, zone1_2.pollutionFactors))
    graph.connect(zone1_1.name, zone1_3.name, calculateRealCost(
        zone1_1.pollutionFactors, zone1_3.pollutionFactors))
    graph.connect(zone1_2.name, zone1_3.name, calculateRealCost(
        zone1_2.pollutionFactors, zone1_3.pollutionFactors))
    graph.connect(zone1_3.name, zone2_2.name, calculateRealCost(
        zone1_3.pollutionFactors, zone2_2.pollutionFactors))
    graph.connect(zone2_1.name, zone2_2.name, calculateRealCost(
        zone2_1.pollutionFactors, zone2_2.pollutionFactors))
    graph.connect(zone2_2.name, zone3_1.name, calculateRealCost(
        zone2_2.pollutionFactors, zone3_1.pollutionFactors))
    graph.connect(zone2_2.name, zone3_2.name, calculateRealCost(
        zone2_2.pollutionFactors, zone3_2.pollutionFactors))
    graph.connect(zone3_1.name, zone3_2.name, calculateRealCost(
        zone3_1.pollutionFactors, zone3_2.pollutionFactors))
    graph.connect(zone3_1.name, zone4_1.name, calculateRealCost(
        zone3_1.pollutionFactors, zone4_1.pollutionFactors))
    graph.connect(zone4_1.name, zone4_2.name, calculateRealCost(
        zone4_1.pollutionFactors, zone4_2.pollutionFactors))
    graph.connect(zone4_2.name, zone4_3.name, calculateRealCost(
        zone4_2.pollutionFactors, zone4_3.pollutionFactors))

    graph.convertToUndirected()
    zones = nodes.copy()
    i = 0

    while (i < (len(zones))):
        if (zones[i].pollution == "veryHigh"):
            graph.remove(zones, zones[i].name)
            zones.pop(i)
            i = i - 1
        i = i + 1

    return graph

# Find path from a Node A to a Node B
def findPath(start, destination):
    startingZone = None
    destinationZone = None
    for i in range(len(nodes)):
        if nodes[i].name.lower() == start.lower():
            startingZone = nodes[i]
        if nodes[i].name.lower() == destination.lower():
            destinationZone = nodes[i]

    if (startingZone == None or destinationZone == None):
        print("Wrong input!")
        return
    graph = generateGraph()

    heuristics = heuristicVector(destinationZone, nodes)

    path = AStarSearch(graph, heuristics, startingZone, destinationZone)
    print(path)

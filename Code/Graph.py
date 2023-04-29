from typing import List, Dict
import numpy as np

class Graph:
    """
    A class representing a graph.

    Attributes:
        graph_dict (dict): A dictionary representing the graph.
        directed (bool): A boolean indicating whether the graph is directed.
    """

    def __init__(self, graph_dict=None, directed=True):
        """
        Initializes the graph.

        Args:
            graph_dict (dict): A dictionary representing the graph.
            directed (bool): A boolean indicating whether the graph is directed.
        """
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.convert_to_undirected()

    def convert_to_undirected(self):
        """
        Converts a directed graph to an undirected graph.
        """
        for a in list(self.graph_dict.keys()):
            for b, dist in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    def add_connection(self, a: str, b: str, distance: int = 1):
        """
        Adds a connection between node A and B with a distance, in the case of an undirected graph, adds an additional
        connection from node B to node A.

        Args:
            a (str): A string representing node A.
            b (str): A string representing node B.
            distance (int): An integer representing the distance between node A and B. Defaults to 1.
        """
        self.graph_dict.setdefault(a, {})[b] = distance
        if not self.directed:
            self.graph_dict.setdefault(b, {})[a] = distance

    def get(self, a: str, b: str = None) -> dict:
        """
        Gets the adjacent nodes.

        Args:
            a (str): A string representing the node to get the adjacent nodes of.
            b (str): A string representing the adjacent node to get the distance of. Defaults to None.

        Returns:
            dict: A dictionary representing the adjacent nodes and their distances.
        """
        connections = self.graph_dict.setdefault(a, {})
        if b is None:
            return connections
        else:
            return connections.get(b)

    def get_nodes(self) -> list:
        """
        Gets a list of nodes.

        Returns:
            list: A list of strings representing the nodes.
        """
        nodes = set(self.graph_dict.keys()) | set(sum(self.graph_dict.values(), {}).keys())
        return list(nodes)

    def remove_node(self, zone_list: list, zone_name: str):
        """
        Removes a node, which is a zone, from the graph.

        Args:
            zone_list (list): A list of zones.
            zone_name (str): A string representing the name of the zone to remove.
        """
        for zone in zone_list:
            if self.graph_dict[zone.name].get(zone_name) is not None:
                self.graph_dict[zone.name].pop(zone_name)
        self.graph_dict.pop(zone_name)
        

class Node:
    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g_cost = 0  # Distance from the start node
        self.h_cost = 0  # Estimated distance to the goal node
        self.f_cost = 0  # Total cost of the node (g_cost + h_cost)

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
         return self.f_cost < other.f_cost

    def __repr__(self):
        return f'({self.name}, {self.f_cost})'


class Zone:
    def __init__(self, name: str):
        self.name = name
        self.pollution_percent = create_pollution()
        self.pollution = assign_pollution(self.pollution_percent)



def create_pollution():
    pollution_percent = np.random.randint(100)
    
    return pollution_percent


def assign_pollution(pollution_percent):
    levels = {0: 'veryLow', 1: 'low', 2: 'moderate', 3: 'high', 4: 'veryHigh'}
    level_index = min(int(pollution_percent / 20), 4)
    return levels[level_index]


#Compute the actual cost of the path from node A to node B.
def calculate_real_cost(start: float, end: float) -> float:
    cost = (start + end) / 2
    return cost

#Estimates the cost of the path from node A to node B.
def  calculate_heuristic(start: float, end: float) -> float:
    heuristic = (start + end) / 2
    return heuristic

#This function is used to find the path from Zone A to Zone B in the graph.
#It returns a vector that stores all the heuristics for the zones that are in between A and B.
def get_heuristics(zona: Zone, nodes: list[Zone]) -> Dict[str, float]:
    return {z.name: calculate_heuristic(zona.pollution_percent, z.pollution_percent) for z in nodes}

#Verify that an adjacent node has been added to the list of nodes yet to be examined (open).
def should_add_neighbor(open: list[Node], neighbor: Node) -> bool:
    for node in open:
        if neighbor == node and neighbor.f_cost >= node.f_cost:
            return False
    return True


# A* Search
def search_a_star(graph: Graph, heuristics: Dict[str, float], start: Zone, goal: Zone) -> List[str]:
    """Finds the shortest path between start and goal using A* search."""
    open_list = []
    closed_list = []
    start_node = Node(start.name, None)
    goal_node = Node(goal.name, None)
    open_list.append(start_node)

    while len(open_list) > 0:
        open_list.sort()
        current_node = open_list.pop(0)
        closed_list.append(current_node)

        if current_node is goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name)
                current_node = current_node.parent
            path.append(start_node.name)
            return list(reversed(path))

        if current_node.name not in graph.graph_dict:
            continue

        for neighbor_name, cost in graph.graph_dict[current_node.name].items():
            neighbor = Node(neighbor_name, current_node)
            if neighbor in closed_list:
                continue
            neighbor.g_cost = current_node.g_cost + cost
            neighbor.h_cost = heuristics.get(neighbor.name)
            neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
            if should_add_neighbor(open_list, neighbor):
                open_list.append(neighbor)

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


#Generate the graph with the corresponding weighted connections between the nodes.
def generateGraph():

    graph = Graph()

    graph.add_connection(zone1_1.name, zone1_2.name, calculate_real_cost(zone1_1.pollution_percent, zone1_2.pollution_percent))
    graph.add_connection(zone1_1.name, zone1_3.name, calculate_real_cost(zone1_1.pollution_percent, zone1_3.pollution_percent))
    graph.add_connection(zone1_2.name, zone1_3.name, calculate_real_cost(zone1_2.pollution_percent, zone1_3.pollution_percent))
    graph.add_connection(zone1_3.name, zone2_2.name, calculate_real_cost(zone1_3.pollution_percent, zone2_2.pollution_percent))
    graph.add_connection(zone2_1.name, zone2_2.name, calculate_real_cost(zone2_1.pollution_percent, zone2_2.pollution_percent))
    graph.add_connection(zone2_2.name, zone3_1.name, calculate_real_cost(zone2_2.pollution_percent, zone3_1.pollution_percent))
    graph.add_connection(zone2_2.name, zone3_2.name, calculate_real_cost(zone2_2.pollution_percent, zone3_2.pollution_percent))
    graph.add_connection(zone3_1.name, zone3_2.name, calculate_real_cost(zone3_1.pollution_percent, zone3_2.pollution_percent))
    graph.add_connection(zone3_1.name, zone4_1.name, calculate_real_cost(zone3_1.pollution_percent, zone4_1.pollution_percent))
    graph.add_connection(zone4_1.name, zone4_2.name, calculate_real_cost(zone4_1.pollution_percent, zone4_2.pollution_percent))
    graph.add_connection(zone4_2.name, zone4_3.name, calculate_real_cost(zone4_2.pollution_percent, zone4_3.pollution_percent))


    graph.convert_to_undirected()
    zones = nodes.copy()
    i = 0

    while (i < (len(zones))):
        if (zones[i].pollution == "veryHigh"):
            graph.remove_node(zones, zones[i].name)
            zones.pop(i)
            i = i - 1
        i = i + 1

    return graph

#Find a path from A to B
def findPath(start, destination):
    startingZone = None
    destinationZone = None
    for i in range(len(nodes)):
        if nodes[i].name.lower() == start.lower():
            startingZone = nodes[i]
        if nodes[i].name.lower() == destination.lower():
            destinationZone = nodes[i]

    if (startingZone == None or destinationZone == None):
        print("Wrong Input!")
        return
    
    graph = generateGraph()

    heuristics  = get_heuristics(destinationZone, nodes)

    path = search_a_star(graph, heuristics , startingZone, destinationZone)
    
    print(path)
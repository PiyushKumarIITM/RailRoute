from collections import defaultdict
from .models import Train
from .my_get_min_switch_route import get_min_switch_route
from .my_trains_for_path import get_trains_by_path
from .my_create_triple_output import create_lists_of_three
from .my_get_optimal_route import find_optimal_route
class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)
        self.initialized = False

    def add_edge(self, u, v):
        self.adjList[u].append(v)  # Directed edge from u to v

    def initialize_graph(self):
        if not self.initialized:
            # Fetch train data once and initialize the graph
            trains = Train.objects.all()
            for train in trains:
                self.add_edge(train.start, train.destination)
            self.initialized = True

    def find_all_paths(self, source, destination):
        current_path = []
        all_paths = []
        visited = {}

        # Initialize all nodes as not visited, including nodes only appearing as destinations
        for node in self.adjList:
            visited[node] = False
            for neighbor in self.adjList[node]:
                if neighbor not in visited:
                    visited[neighbor] = False

        self.dfs(source, destination, visited, current_path, all_paths)

        return all_paths

    def dfs(self, current_node, destination, visited, current_path, all_paths):
        visited[current_node] = True
        current_path.append(current_node)

        if current_node == destination:
            all_paths.append(list(current_path))
        else:
            for neighbor in self.adjList[current_node]:
                if not visited.get(neighbor, False):
                    self.dfs(neighbor, destination, visited, current_path, all_paths)

        # Backtrack
        current_path.pop()
        visited[current_node] = False

# Singleton instance of the Graph class
graph_instance = Graph()

# Function to find routes
def find_route_func(source, destination, day):
    # Initialize graph if not done already
    graph_instance.initialize_graph()

    # Find and return all paths
    all_paths = graph_instance.find_all_paths(source, destination)
    unique_tuples = set(tuple(lst) for lst in all_paths)

    # Convert tuples back to lists if needed
    unique_lists_of_paths = [list(tpl) for tpl in unique_tuples]
    list_of_lists_trains=[]
    for path1 in unique_lists_of_paths:
        # print(path1)
        list_trains = get_trains_by_path(path1)
        list_of_lists_trains.append(list_trains)

    trains_route_list_with_start_st = get_min_switch_route(list_of_lists_trains)
    optimal_list = find_optimal_route(trains_route_list_with_start_st)
    list2 = create_lists_of_three(optimal_list,destination)

    # return unique_lists
    return list2

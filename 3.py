import networkx as nx
import matplotlib.pyplot as plt
from classes.gbfs import GbfsTraverser

G = nx.Graph()
nodes = ["SC", "Siwaka", "Ph.1A", "Ph.1B", "Phase2",
         "J1", "Mada", "ParkingLot", "Phase3", "STC"]
G.add_nodes_from(nodes)
G.nodes()

# add Edges and their weights
G.add_edge("SC", "Siwaka", weight=450)
G.add_edge("Siwaka", "Ph.1A", weight=10)
G.add_edge("Siwaka", "Ph.1B", weight=230)
G.add_edge("Ph.1A", "Ph.1B", weight=100)
G.add_edge("Ph.1A", "Mada", weight=850)
G.add_edge("Ph.1B", "Phase2", weight=112)
G.add_edge("Ph.1B", "STC", weight=50)
G.add_edge("Phase2", "STC", weight=50)
G.add_edge("Phase2", "J1", weight=600)
G.add_edge("Phase2", "Phase3", weight=500)
G.add_edge("STC", "ParkingLot", weight=250)
G.add_edge("Phase3", "ParkingLot", weight=350)
G.add_edge("Mada", "ParkingLot", weight=700)
G.add_edge("Mada", "J1", weight=200)

# position the nodes to resemble Madaraka Estate Network
G.nodes["SC"]['pos'] = (0, 0)
G.nodes["Siwaka"]['pos'] = (1, 0)
G.nodes["Ph.1A"]['pos'] = (2, 0)
G.nodes["Ph.1B"]['pos'] = (2, -1)
G.nodes["STC"]['pos'] = (2, -2)
G.nodes["Phase2"]['pos'] = (3, -1)
G.nodes["J1"]['pos'] = (4, -1)
G.nodes["Phase3"]['pos'] = (4, -2)
G.nodes["Mada"]['pos'] = (5, -1)
G.nodes["ParkingLot"]['pos'] = (4, -3)

# store all positions in a variable
node_pos = nx.get_node_attributes(G, 'pos')
arc_weight = nx.get_edge_attributes(G, 'weight')

# call BFS to return set of all possible routes to the goal
route_bfs = GbfsTraverser()
routes = route_bfs.gbfs(G, "SC", "ParkingLot")
print(route_bfs.visited)
route_list = route_bfs.visited

# color the nodes and edges in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_edges = list(zip(route_list, route_list[1:]))
edge_col = ['darkturquoise' if not edge in peru_edges else 'peru' for edge in G.edges()]

# draw network
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=1000)
nx.draw_networkx_edges(G, node_pos, width=1, edge_color=edge_col)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
# nx.draw_networkx_edge_labels(G, node_pos, edge_color=edge_col, edge_labels=arc_weight)

# display
plt.axis('off')
plt.show()

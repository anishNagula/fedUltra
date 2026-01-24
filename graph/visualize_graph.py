import pickle
import networkx as nx
import matplotlib.pyplot as plt
import random

# load graph
with open("data/processed/lanl_graph.pkl", "rb") as f:
    graph = pickle.load(f)

# --- STEP 1: sample edges, not nodes ---
all_edges = list(graph.edges())
sampled_edges = random.sample(all_edges, 10)

# --- STEP 2: collect connected nodes ---
nodes = set()
for u, v in sampled_edges:
    nodes.add(u)
    nodes.add(v)

subgraph = graph.subgraph(nodes)

print("Visualizing subgraph")
print("Nodes:", subgraph.number_of_nodes())
print("Edges:", subgraph.number_of_edges())

# --- STEP 3: color nodes by type ---
node_colors = []
for node in subgraph.nodes():
    ntype = subgraph.nodes[node]["node_type"]
    node_colors.append("tab:blue" if ntype == "user" else "tab:orange")

# --- STEP 4: draw ---
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(subgraph, seed=42)

nx.draw(
    subgraph,
    pos,
    node_color=node_colors,
    node_size=500,
    edge_color="gray",
    arrows=True,
    with_labels=False,
)

plt.title("LANL Auth Graph – 10 Edge Subgraph")
plt.show()

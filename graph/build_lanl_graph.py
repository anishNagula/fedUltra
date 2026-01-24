from graph.build_graph import GraphBuilder
import networkx as nx
from collections import Counter
import pickle

if __name__ == "__main__":
    builder = GraphBuilder()

    graph = builder.build_from_lanl_file(
        "data/raw/lanl-auth-dataset-1-00.bz2",
        max_lines=100_000
    )

    print("Graph built")
    print("Nodes:", graph.number_of_nodes())
    print("Edges:", graph.number_of_edges())

    # sanity checks
    node_types = Counter(nx.get_node_attributes(graph, "node_type").values())
    edge_types = Counter(nx.get_edge_attributes(graph, "relation").values())

    print("Node types:", node_types)
    print("Edge types:", edge_types)

    # persist graph
    with open("data/processed/lanl_graph.pkl", "wb") as f:
        pickle.dump(graph, f)

    print("Graph saved to data/processed/lanl_graph.pkl")


import pickle
import torch
import networkx as nx
from torch_geometric.data import Data


def nx_to_pyg(graph: nx.DiGraph) -> Data:
    num_nodes = graph.number_of_nodes()

    # node features: [in_degree, out_degree]
    x = torch.zeros((num_nodes, 2), dtype = torch.float)

    for node, attrs in graph.nodes(data = True):
        x[node, 0] = attrs.get("in_degree", 0)
        x[node, 1] = attrs.get("out_degree", 0)

    edge_index = torch.tensor(list(graph.edges()), dtype = torch.long).t().contiguous()

    return Data(x = x, edge_index = edge_index)


if __name__ == "__main__":
    with open("data/processed/lanl_graph.pkl", "rb") as f:
        graph = pickle.load(f)

    data = nx_to_pyg(graph)
    torch.save(data, "data/processed/lanl_graph.pt")

    print("Saved PyG graph:")
    print(data)
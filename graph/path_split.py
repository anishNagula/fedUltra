import pickle
import networkx as nx
from collections import deque, defaultdict

MAX_DEPTH = 3

def bfs_max_depth(graph, source, max_depth=3):
    """
    Bounded BFS.
    Returns the maximum depth reachable from source (capped at max_depth).
    """
    visited = set([source])
    queue = deque([(source, 0)])
    max_reached = 0

    while queue:
        node, depth = queue.popleft()
        max_reached = max(max_reached, depth)

        if depth == max_depth:
            continue

        for nbr in graph.successors(node):
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, depth + 1))

    return max_reached


def main():
    with open("data/processed/lanl_flow_graph.pkl", "rb") as f:
        graph = pickle.load(f)

    depth_bucket = defaultdict(set)

    print("Computing bounded BFS depths...")

    for node in graph.nodes():
        d = bfs_max_depth(graph, node, MAX_DEPTH)
        depth_bucket[d].add(node)

    # training safe nodes (depth <= 2)
    training_nodes = set()
    for d in [0, 1, 2]:
        training_nodes |= depth_bucket[d]

    # zero day (depth >= 3)
    test_nodes = set()
    for d in depth_bucket:
        if d >= 3:
            test_nodes |= depth_bucket[d]

    print("=== Path-based Split Summary ===")
    print(f"Total nodes            : {graph.number_of_nodes()}")
    print(f"Training-safe nodes ≤2 : {len(training_nodes)}")
    print(f"Zero-day nodes ≥3      : {len(test_nodes)}")

    # build training graph (induced subgraph)
    train_graph = graph.subgraph(training_nodes).copy()

    print("\nTraining graph:")
    print(f"Nodes: {train_graph.number_of_nodes()}")
    print(f"Edges: {train_graph.number_of_edges()}")


    with open("data/processed/train_graph.pkl", "wb") as f:
        pickle.dump(train_graph, f)

    with open("data/processed/test_nodes.pkl", "wb") as f:
        pickle.dump(test_nodes, f)

    print("\nSaved:")
    print(" - data/processed/train_graph.pkl")
    print(" - data/processed/test_nodes.pkl")


if __name__ == "__main__":
    main()

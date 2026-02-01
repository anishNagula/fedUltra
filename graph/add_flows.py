import pickle
from collections import defaultdict
from graph.schema import NodeType, RelationType

TIME_WINDOW = 30 * 60  # 30 minutes

def main():
    with open("data/processed/lanl_graph.pkl", "rb") as f:
        graph = pickle.load(f)

    # user -> list of (timestamp, host)
    user_sessions = defaultdict(list)

    for u, h, data in graph.edges(data=True):
        if data["relation"] == RelationType.AUTHENTICATES_TO.value:
            user_sessions[u].append((data["timestamp"], h))

    flow_edges = 0

    for user, events in user_sessions.items():
        events.sort()  # sort by time

        for i in range(len(events) - 1):
            t1, h1 = events[i]
            t2, h2 = events[i + 1]

            if t2 - t1 <= TIME_WINDOW and h1 != h2:
                graph.add_edge(
                    h1,
                    h2,
                    relation=RelationType.FLOWS_TO.value,
                    timestamp=t2
                )
                flow_edges += 1

    print(f"Added {flow_edges} HOST→HOST flow edges")

    with open("data/processed/lanl_flow_graph.pkl", "wb") as f:
        pickle.dump(graph, f)

    print("Saved enriched graph to data/processed/lanl_flow_graph.pkl")

if __name__ == "__main__":
    main()

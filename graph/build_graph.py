import networkx as nx
import bz2
from typing import Dict, Optional

from graph.schema import NodeType, RelationType



class GraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.node_map: Dict[str, int] = {}
        self.next_node_id = 0

    def _get_or_create_node(self, entity: str, node_type: NodeType) -> int:
        """
        Create or fetch a node ID.
        Namespacing by node_type avoids collisions (e.g., USER:U1 vs HOST:U1).
        """

        key = f"{node_type.value}:{entity}"

        if key not in self.node_map:
            node_id = self.next_node_id
            self.node_map[key] = node_id
            self.next_node_id += 1

            self.graph.add_node(
                node_id,
                entity=entity,
                node_type=node_type.value,
                in_degree=0,
                out_degree=0,
            )

        return self.node_map[key]

    def add_edge(
        self,
        src_entity: str,
        dst_entity: str,
        src_type: NodeType,
        dst_type: NodeType,
        relation: RelationType,
        timestamp: int
    ):
        src_id = self._get_or_create_node(src_entity, src_type)
        dst_id = self._get_or_create_node(dst_entity, dst_type)

        self.graph.add_edge(
            src_id,
            dst_id,
            relation = relation.value,
            timestamp = timestamp,
        )

        self.graph.nodes[src_id]["out_degree"] += 1
        self.graph.nodes[dst_id]["in_degree"] += 1

    def build_from_lanl_file(
        self,
        file_path: str,
        max_lines: Optional[int] = None,
    ):
        """
        Build graph from LANL authentication log (.bz2).
        Format per line:
        timestamp,user,computer
        Example:
        1,U1,C1
        """

        with bz2.open(file_path, "rt") as f:
            for i, line in enumerate(f):
                if max_lines is not None and i >= max_lines:
                    break

                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue    # skip malformed lines

                ts_str, user, computer = parts

                try:
                    timestamp = int(ts_str)
                except ValueError:
                    continue

                self.add_edge(
                    src_entity = user,
                    dst_entity = computer,
                    src_type = NodeType.USER,
                    dst_type = NodeType.HOST,
                    relation = RelationType.AUTHENTICATES_TO,
                    timestamp = int(timestamp),
                )

        return self.graph
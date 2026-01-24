import pandas as pd
import networkx as nx
from typing import Dict

from graph.schema import NodeType, RelationType



class GraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.node_map: Dict[str, int] = {}
        self.next_node_id = 0

    def _get_or_create_node(self, entity: str, node_type: NodeType) -> int:
        if entity not in self.node_map:
            node_id = self.next_node_id
            self.node_map[entity] = node_id
            self.next_node_id += 1

            self.graph.add_node(
                node_id,
                entity = entity,
                node_type = node_type.value
            )
        
        return self.node_map[entity]

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

    def build_from_dataframe(self, df: pd.DataFrame):
        for _, row in df.iterrows():
            self.add_edge(
                src_entity = row["src"],
                dst_entity = row["dst"],
                src_type = NodeType.USER,
                dst_type = NodeType.HOST,
                relation = RelationType.AUTHENTICATES_TO,
                timestamp = int(row["timestamp"])
            )

        return self.graph

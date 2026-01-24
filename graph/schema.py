from enum import Enum
from dataclasses import dataclass
from typing import Dict, List


# node types
class NodeType(str, Enum):
    USER = "user"
    HOST = "host"
    SERVICE = "service"

# relation types
class RelationType(str, Enum):
    AUTHENTICATES_TO = "authenticates_to"
    ACCESSES = "accesses"
    ESCALATES_PRIVILEGE_ON = "escalates_on"


# feature definitions
@dataclass
class NodeFeatures:
    node_type: NodeType
    in_degree: int = 0
    out_degree: int = 0
    is_admin: bool = False


@dataclass
class EdgeFeatures:
    relation_type: RelationType
    timestamp: int



NODE_FEATURE_DIMENSIONS: Dict[str, int] = {
    "node_type": len(NodeType),
    "in_degree": 1,
    "out_degree": 1,
    "is_admin": 1,
}


EDGE_FEATURE_DIMENSIONS: Dict[str, int] = {
    "relation_type": len(RelationType),
    "timestamp": 1,
}


# allowed relations
ALLOWED_RELATIONS: Dict[RelationType, List[NodeType]] = {
    RelationType.AUTHENTICATES_TO: [NodeType.USER, NodeType.HOST],
    RelationType.ACCESSES: [NodeType.HOST, NodeType.HOST],
    RelationType.ESCALATES_PRIVILEGE_ON: [NodeType.USER, NodeType.HOST],
}


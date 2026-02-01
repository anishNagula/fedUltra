# FedUltra – Phase 2 Implementation

This repository contains the **Phase-2 implementation** of our capstone project.  
Current focus is on **graph construction and centralized baseline validation** using LANL authentication logs.

---

## Completed So Far

- Parsed LANL authentication logs (`.bz2`)
- Built a typed directed graph (USER → HOST)
- Defined a domain-driven graph schema (nodes, relations, features)
- Added basic validation and visualization utilities
- Converted NetworkX graphs to PyTorch Geometric format
- Implemented and ran a centralized **GraphSAGE** baseline (pipeline validation)
- **Enriched authentication graphs with time-based HOST → HOST flow edges**
- **Operationalized zero-day definition using path-based train/test split**
  - Training-safe nodes: paths ≤ 2 hops  
  - Zero-day candidates: paths ≥ 3 hops  

> Current implementation focuses on **pipeline correctness and structural setup**.  
> No anomaly scoring, ULTRA evaluation, or federation yet.

---

## Project Structure

```text
fedUltra/
├── graph/            # Schema, construction, enrichment, splitting, visualization
├── models/           # GraphSAGE model
├── experiments/      # Training scripts
├── data/             # Ignored (raw + processed data)
├── requirements.txt
└── README.md
```

---

## Setup

```bash
git clone "https://github.com/anishNagula/fedUltra"
cd fedUltra
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage
### Read dataset
```bash
python -m graph.test_read_lanl
```

### Build base authentication graph
```bash
python -m graph.build_lanl_graph
```

### Add time-based flow enrichment (HOST → HOST)
```bash
python -m graph.add_flows
```

### Perform path-based train/test split
```bash
python -m graph.path_split
```

### Visualize small subgraph
```bash
python -m graph.visualize_graph
```

### Convert to PyTorch Geometric format
```bash
python -m graph.nx_to_pyg
```

### Run centralized GraphSAGE baseline (validation only)
```bash
python -m experiments.train_graphsage
```

---
## Current Status
- End-to-end graph pipeline validated
- Time-based flow graphs constructed
- Zero-day candidates identified via structural paths
- Centralized GraphSAGE baseline runs successfully

Next steps include training on the restricted graph, anomaly scoring, and ULTRA-based evaluation, followed by federated extensions.
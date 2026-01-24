# FedUltra – Phase 2 Implementation

This repository contains the **Phase-2 implementation** of our capstone project.  
Current focus is on **graph construction and centralized baseline validation** using LANL authentication logs.

---

## Completed So Far

- Parsed LANL authentication logs (`.bz2`)
- Built a typed directed graph (USER → HOST)
- Added basic validation and visualization
- Converted graph to PyTorch Geometric format
- Implemented and ran a centralized GraphSAGE baseline (pipeline validation only)

> No anomaly detection, zero-day evaluation, or federation yet.

---

## Project Structure

```text
fedUltra/
├── graph/            # Graph schema, construction, conversion, visualization
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

### Build graph
```bash
python -m graph.build_lanl_graph
```

### Visualize small subgraph
```bash
python -m graph.visualize_graph
```

### Convert to PyG format
```bash
python -m graph.nx_to_pyg
```

### Run centralized GraphSAGE baseline
```bash
python -m experiments.train_graphsage
```

---
## Current Status
- End-to-end pipeline runs successfully
- Centralized Baseline Validated
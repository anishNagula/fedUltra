import torch
from torch.optim import Adam

from models.graphsage import GraphSAGE

data = torch.load("data/processed/lanl_graph.pt")

model = GraphSAGE(
    in_channels = data.x.size(1),
    hidden_channels = 32,
)

optimizer = Adam(model.parameters(), lr = 0.01)

model.train()
for epoch in range(10):
    optimizer.zero_grad()
    out = model(data)
    loss = out.norm(p = 2)
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch} | loss = {loss.item():.4f}")
import torch
import torch.nn as nn
import torch.optim as optim

def train_model(model, X_train, y_train, X_test, y_test, epochs=50, lr=0.001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    losses = []

    for epoch in range(epochs):
        model.train()
        inputs = torch.FloatTensor(X_train)
        targets = torch.FloatTensor(y_train).view(-1, 1)
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        losses.append(loss.item())

    model.eval()
    with torch.no_grad():
        test_inputs = torch.FloatTensor(X_test)
        predictions = model(test_inputs).view(-1)
        test_loss = criterion(predictions, torch.FloatTensor(y_test))

    return losses, test_loss.item(), predictions.numpy()

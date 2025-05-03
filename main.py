import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from vesicle_ann import encapsulate_memory_block
from model import SimpleANN
from train import train_model
from data_utils import generate_data

def test_all_modes():
    X_raw, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X_raw, y, test_size=0.2)

    results = {}
    modes = ['raw', 'keyed', 'noise_filter', 'scale_compress']
    for mode in modes:
        print(f"\n--- Testing mode: {mode} ---")
        if mode == 'raw':
            X_enc_train = X_train
            X_enc_test = X_test
        else:
            X_enc_train = encapsulate_memory_block(X_train, mode=mode)
            X_enc_test = encapsulate_memory_block(X_test, mode=mode)

        model = SimpleANN(input_size=1)
        losses, test_loss, preds = train_model(model, X_enc_train, y_train, X_enc_test, y_test)
        accuracy = np.mean((preds > 0.5) == y_test)
        results[mode] = {'loss': losses, 'test_loss': test_loss, 'accuracy': accuracy}
        print(f"Test loss: {test_loss:.4f}, Accuracy: {accuracy*100:.2f}%")

    # Plot
    plt.figure(figsize=(10, 6))
    for mode in modes:
        label = f"{'Simple ANN' if mode == 'raw' else 'Encapsulated'} ({mode} Acc: {results[mode]['accuracy']*100:.2f}%)"
        plt.plot(results[mode]['loss'], label=label)
    plt.xlabel("Epoch")
    plt.ylabel("Training Loss")
    plt.title("Loss Curve Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return results

if __name__ == "__main__":
    final_results = test_all_modes()


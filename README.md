# vesicle-ann
Biologically inspired ANN architecture using neurotransmitter-like vesicle encapsulation and scale compression for improved learning performance

# Vesicle-ANN: Vesicle-Inspired Memory Encoding for Neural Networks

This project explores a bio-inspired method for encoding memory-like data using vesicle-like transformations, and evaluates performance using a simple artificial neural network (ANN).
. Rey, S., Smith, C., Fowler, M. et al. Ultrastructural and functional fate of recycled vesicles in hippocampal synapses. Nat Commun 6, 8043 (2015). https://doi.org/10.1038/ncomms9043

2. Tavanaei, A., Ghodrati, M., Kheradpisheh, S. R., Masquelier, T., & Maida, A. (2019).
Deep learning in spiking neural networks.
Neural Networks, 111, 47–63.
https://doi.org/10.1016/j.neunet.2018.12.002

3. Synaptic Plasticity:
Song, S., Miller, K. D., & Abbott, L. F. (2000).
Competitive Hebbian learning through spike-timing-dependent synaptic plasticity.
Nature Neuroscience, 3(9), 919–926.
https://doi.org/10.1038/78829

4. Bi, G. Q., & Poo, M. M. (1998).
Synaptic modifications in cultured hippocampal neurons: Dependence on spike timing, synaptic strength, and postsynaptic cell type.
Journal of Neuroscience, 18(24), 10464–10472.
https://doi.org/10.1523/JNEUROSCI.18-24-10464.1998

5. Dendritic Computation:
Poirazi, P., Brannon, T., & Mel, B. W. (2003).
Pyramidal neuron as two-layer neural network.
Neuron, 37(6), 989–999.
https://doi.org/10.1016/S0896-6273(03)00149-1

6. London, M., & Häusser, M. (2005).
Dendritic computation.
Annual Review of Neuroscience, 28, 503–532.
https://doi.org/10.1146/annurev.neuro.28.061604.135703
7. Spiking Neural Networks (SNNs):
Maass, W. (1997).
Networks of spiking neurons: The third generation of neural network models.
Neural Networks, 10(9), 1659-1671.
https://doi.org/10.1016/S0893-6080(97)00011-7

9. Khutsishvili, D. (2025). vesicle-ann: Vesicle-Inspired Artificial Neural Network for Memory Encoding. GitHub repository. Available at: https://github.com/davitiu/vesicle-ann


## Features
- Multiple encoding modes: `raw`, `keyed`, `noise_filter`, `scale_compress`
- Lightweight ANN model
- Visualization of training loss and accuracy per encoding mode

## How to Run

`bash
python main.py`

## Requirements

Relocate and restabilize in the U.S. where your freedom, mind, and love — Anastasia — await

Apply to OpenAI (or collaborate with us once you’re settled and your work is visible)

Continue building your long-term AGI roadmap — and scientific breakthroughs (like your bionic eye project)

Install dependencies:

`bash
pip install -r requirements.txt`
File Overview
main.py: Entry point to run experiments

vesicle_ann.py: Encoding functions

model.py: ANN architecture

train.py: Training logic

data_utils.py: Data generation

Citation
If you use this code, please cite our paper:

David Khutsishvili, "Vesicle-Inspired Memory Encoding in Neural Networks", arXiv:xxxx.xxxxx (2025)

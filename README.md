# vesicle-ann
Biologically inspired ANN architecture using neurotransmitter-like vesicle encapsulation and scale compression for improved learning performance

# Vesicle-ANN: Vesicle-Inspired Memory Encoding for Neural Networks

This project explores a bio-inspired method for encoding memory-like data using vesicle-like transformations, and evaluates performance using a simple artificial neural network (ANN).

## Features
- Multiple encoding modes: `raw`, `keyed`, `noise_filter`, `scale_compress`
- Lightweight ANN model
- Visualization of training loss and accuracy per encoding mode

## How to Run

`bash
python main.py`

Requirements
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

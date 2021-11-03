#!/bin/bash

# Add cuda 10.1 DLLs to library path and set GPU
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.1/lib64
export CUDA_VISIBLE_DEVICES=1

# If using virtualenv, activate environment
source path/to/env/bin/activate

python3 tf-test.py

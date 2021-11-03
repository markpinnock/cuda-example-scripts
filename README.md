Example shell scripts for linking CUDA DLLs to Tensorflow or Pytorch on a shared GPU cluster
[https://github.com/markpinnock/cuda-example-scripts]

## CUDA DLLs
Tensorflow and Pytorch both require CUDA to be linked at runtime (e.g. cuBLAS, cuDNN). This is performed automatically by conda (which installs the CUDA Toolkit containing the DLLs and also cuDNN) but to save space in the users' home directories these can be kept in a shared location (e.g. /usr/local). On Linux they can then be linked by setting the LD_LIBRARY_PATH environment variable either in Python using `os.environ["LD_LIBRARY_PATH"] = "/usr/local/cuda-10.1` or in a shell script that then calls your program.

## Pytorch
This shell script is tested with Pytorch 1.8 and CUDA 11.2 with cuDNN 8.1. Compatibilities for previous versions can be found here[https://pytorch.org/get-started/previous-versions/].

## Tensorflow
There are two shell scripts, one for Tensorflow 2.3 and one for Tensorflow 2.5 (using CUDA 10.1 with cuDNN 7.6 and CUDA 11.2 with cuDNN 8.1 respectively). The compatibility matrix for other versions can be found here[https://www.tensorflow.org/install/source#gpu].

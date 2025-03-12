# https://pytorch.org/get-started
# pip3 install torch torchvision torchaudio

import torch
from d2l import torch as d2l

def try_gpu(i = 0):
    if torch.cuda.device_count() >= i + 1:
        return torch.device(f"cuda:{i}")
    return torch.device("cpu")

def try_all_gpus():
    return [torch.device(f"cuda:{i}") for i in range(torch.cuda.device_count())]

if __name__ == "__main__":
    print("CUDA is is_available: ", torch.cuda.is_available())

    # CUDA: host - CPU, device - GPU
    # $ nvidia-smi
    # x = torch.rand(5, 3) # assigned to the CPU context by default
    x = torch.ones(5, 3, device=try_gpu())
    print("x: ", x)
    print("x.device:", x.device)

    # print(d2l.cpu(), d2l.gpu(), d2l.gpu(1))
    print(torch.device('cpu'), torch.device('cuda:0'), torch.device('cuda:1'))
    # создается объект независимо от того, есть ли физическое устройство

    # Number of available GPUs
    print("Total num of GPUs: ", torch.cuda.device_count())

    print("try_gpu(0): ",       try_gpu(0))
    print("try_gpu(1): ",       try_gpu(1))
    print("try_all_gpus(): ",   try_all_gpus())


"""
Output:

CUDA is is_available:  True
x:  tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]], device='cuda:0')
x.device: cuda:0
cpu cuda:0 cuda:1
Total num of GPUs:  1
try_gpu(0):  cuda:0
try_gpu(1):  cpu
try_all_gpus():  [device(type='cuda', index=0)]
"""

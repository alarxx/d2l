# https://pytorch.org/get-started
# pip3 install torch torchvision torchaudio

import torch

if __name__ == "__main__":
    print("CUDA is is_available: ", torch.cuda.is_available())

    x = torch.rand(5, 3)
    print(x)


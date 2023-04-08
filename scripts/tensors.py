import torch
import numpy as np
import matplotlib.pyplot as plt

# from pure python list to tensor
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(f"Tensor from python list: {x_data} \n")

# from numpy array to tensor
np_array = np.array(data, dtype=np.float32)
x_np = torch.from_numpy(np_array)
print(f"Tensor from numpy array: {x_np} \n")

x_ones = torch.ones_like(x_data)  # retains the properties of x_data
print(f"Ones Tensor: {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)  # overrides the datatype of x_data
print(f"Random Tensor: {x_rand} \n")

import torch

print(torch.__version__)

x = torch.rand(5, 3)
#print(x)

# Scalar
scalar = torch.tensor(7) # 7 is a scalar with tensor type and rank 0
#print(scalar)
#print(scalar.ndim) # prints the dimension of the tensor

vector = torch.tensor([1, 2, 3, 4, 5]) # 1D tensor
#print(vector.ndim)
#print(vector.shape)

MATRIX = torch.tensor([[1, 2, 3], [4, 5, 6]]) # 2D tensor, two square brackets
#print(MATRIX.ndim)
print(MATRIX[0]) # prints the first row, index starts from 0

# 3D tensor and higher
TENSOR_3D = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])


# Import the torch library
import torch

def main():
    # Task 1: Tensor Creation
    # Create a 1D tensor of size 10 filled with zeros
    tensor_1d = torch.zeros(10)
    print("Tensor 1D of zeros: ", tensor_1d)

    # Create a 2D tensor of size 3x3 filled with random numbers from a uniform distribution
    tensor_2d = torch.rand(3, 3)
    print("Tensor 2D: ", tensor_2d)

    # Create a tensor from a Python list of numbers
    tensor_from_list = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Tensor from list: ", tensor_from_list)
    

    # Task 2: Tensor Operations
    # Perform element-wise addition and multiplication on tensors
    add_result = tensor_1d + tensor_from_list
    print("Addition result from Tensor 1D and Tensor from list: ", add_result)
    multiply_result = tensor_1d * tensor_from_list
    print("Multiplication result from Tensor 1D and Tensor from list: ", multiply_result)

    # Calculate the mean and standard deviation of a tensor
    tensor_mean = torch.mean(tensor_from_list.float())
    print("Mean of Tensor from list: ", tensor_mean)
    tensor_std = torch.std(tensor_from_list.float())
    print("Standard deviation of Tensor from list: ", tensor_std)

    # Resize/reshape a tensor to a different shape
    reshaped_tensor = tensor_2d.reshape(1, 9)
    print("Reshaped Tensor 2D: ", reshaped_tensor)

    # Task 3: Tensor Indexing
    # Select the second element from the 1D tensor
    second_element = tensor_from_list[1]
    print("Second element from Tensor from list: ", second_element)

if __name__ == '__main__':
    main()

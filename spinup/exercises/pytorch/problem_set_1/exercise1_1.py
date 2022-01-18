import torch
import numpy as np

"""

Exercise 1.1: Diagonal Gaussian Likelihood

Write a function that takes in PyTorch Tensors for the means and 
log stds of a batch of diagonal Gaussian distributions, along with a 
PyTorch Tensor for (previously-generated) samples from those 
distributions, and returns a Tensor containing the log 
likelihoods of those samples.

"""

def gaussian_likelihood(x, mu, log_std):
    """
    Args:
        x: Tensor with shape [batch, dim]
        mu: Tensor with shape [batch, dim]
        log_std: Tensor with shape [batch, dim] or [dim]

    Returns:
        Tensor with shape [batch]
    """
    # Referencing the Log-Likelihood equation from the [documentation](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
    batch, dim = x.shape
    
    squared_diff = (x - mu)**2 # shape [batch, dim]
    std = torch.exp(log_std) # shape [batch, dim] or [dim]

    # I had to check with the solution to figure out I needed to add 1E-8 to std
    diff_std_ratio = squared_diff / (std + 1E-8)**2 # shape [batch, dim]

    summed = torch.sum(diff_std_ratio + 2*log_std, dim=1) # shape [batch]
    log_likelihood = -0.5*(summed + dim*np.log(2*np.pi)) # shape [batch]
    return log_likelihood


if __name__ == '__main__':
    """
    Run this file to verify your solution.
    """
    from spinup.exercises.pytorch.problem_set_1_solutions import exercise1_1_soln
    from spinup.exercises.common import print_result

    batch_size = 32
    dim = 10

    x = torch.rand(batch_size, dim)
    mu = torch.rand(batch_size, dim)
    log_std = torch.rand(dim)

    your_gaussian_likelihood = gaussian_likelihood(x, mu, log_std)
    true_gaussian_likelihood = exercise1_1_soln.gaussian_likelihood(x, mu, log_std)

    your_result = your_gaussian_likelihood.detach().numpy()
    true_result = true_gaussian_likelihood.detach().numpy()

    correct = np.allclose(your_result, true_result)
    print_result(correct)
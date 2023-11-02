import numpy as np

def power_method(A, initial_vector, max_iterations=5):
    n = A.shape[0]
    x = initial_vector / np.linalg.norm(initial_vector)  # Normalize the initial vector

    for i in range(max_iterations):
        y = A @ x
        eigenvalue = np.max(np.abs(y))
        x = y / eigenvalue

        # Print the iteration details
        print(f"Iteration {i + 1}:")
        print("Vector:", np.round(y, decimals=4))
        print("Normalized Vector:", np.round(x, decimals=4))
        print()

    return eigenvalue, x

# Define the matrix and initial vector
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]])
initial_vector = np.array([1, 0, 0])

# Apply the power method
eigenvalue, eigenvector = power_method(A, initial_vector)

print("Largest Eigenvalue:", round(eigenvalue, 4))
print("Eigenvector:", np.round(eigenvector, decimals=4))

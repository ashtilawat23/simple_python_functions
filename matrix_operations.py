# complex_math_operations.py

import numpy as np

def matrix_operations(matrix):
    """
    Performs complex mathematical operations on the given matrix:
    matrix multiplication, determinant calculation, and finding
    eigenvalues and eigenvectors.

    :param matrix: 2D list, input matrix to be analyzed
    :return: dict, results of the mathematical operations
    """
    # Convert the input matrix to a NumPy array
    np_matrix = np.array(matrix)
    
    # Ensure the matrix is square for determinant and eigenvalue operations
    if np_matrix.shape[0] != np_matrix.shape[1]:
        raise ValueError("Matrix must be square for determinant and eigenvalue calculations.")
    
    # Matrix multiplication (matrix squared)
    matrix_mult = np.matmul(np_matrix, np_matrix)
    
    # Determinant of the matrix
    matrix_det = np.linalg.det(np_matrix)
    
    # Eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(np_matrix)
    
    # Prepare results
    results = {
        'matrix_mult': matrix_mult,
        'matrix_det': matrix_det,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }
    
    return results

def main():
    matrix = [
        [4, 2, 3],
        [3, 5, 7],
        [1, 2, 4]
    ]
    
    results = matrix_operations(matrix)
    print("Matrix Operations Results:")
    print(f"Matrix Squared:\n{results['matrix_mult']}")
    print(f"Determinant: {results['matrix_det']}")
    print(f"Eigenvalues: {results['eigenvalues']}")
    print(f"Eigenvectors:\n{results['eigenvectors']}")

if __name__ == "__main__":
    main()

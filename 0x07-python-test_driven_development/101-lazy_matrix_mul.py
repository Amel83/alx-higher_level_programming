import numpy as np


def lazy_matrix_mul(m_a, m_b):
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("Matrices cannot be multiplied")

    result = np.matmul(matrix_a, matrix_b)
    return result.tolist()

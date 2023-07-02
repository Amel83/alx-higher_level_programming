#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    m_a_rows = len(m_a)
    m_a_cols = len(m_a[0])
    m_b_rows = len(m_b)
    m_b_cols = len(m_b[0])

    if m_a_cols != m_b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(m_b_cols)] for _ in range(m_a_rows)]

    for i in range(m_a_rows):
        for j in range(m_b_cols):
            for k in range(m_a_cols):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

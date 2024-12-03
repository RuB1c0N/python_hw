import numpy as np
from matrix_library.mixins import MatrixMixin

class Matrix(MatrixMixin):
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            raise ValueError("Неверный формат матриц")
        self.data = data

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Размерности матриц должны совпадать для сложения.")
        result = np.zeros(self.data.shape, dtype=self.data.dtype)
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                result[i, j] = self.data[i, j] + other.data[i, j]
        return Matrix(result)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Размерности матриц должны совпадать для покомпонентного умножения.")
        result = np.zeros(self.data.shape, dtype=self.data.dtype)
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                result[i, j] = self.data[i, j] * other.data[i, j]
        return Matrix(result)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Размерности матриц несовместимы для матричного умножения.")
        result = np.zeros((self.data.shape[0], other.data.shape[1]), dtype=self.data.dtype)
        for i in range(self.data.shape[0]):
            for j in range(other.data.shape[1]):
                for k in range(self.data.shape[1]):
                    result[i, j] += self.data[i, k] * other.data[k, j]
        return Matrix(result)

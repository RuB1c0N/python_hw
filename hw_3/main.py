import numpy as np
import os
from matrix_library.matrix import Matrix


def generate_matrix_data():
    np.random.seed(0)
    matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))
    return matrix_a, matrix_b


def save_matrices(matrix_a, matrix_b, matrix_add, matrix_mul, matrix_matmul, task_number):
    os.makedirs(f"./artifacts/{task_number}", exist_ok=True)

    matrix_a.save_to_file(f"./artifacts/{task_number}/matrix_a.txt")
    matrix_b.save_to_file(f"./artifacts/{task_number}/matrix_b.txt")
    matrix_add.save_to_file(f"./artifacts/{task_number}/matrix+.txt")
    matrix_mul.save_to_file(f"./artifacts/{task_number}/matrix*.txt")
    matrix_matmul.save_to_file(f"./artifacts/{task_number}/matrix@.txt")


def task_3_1():
    matrix_a, matrix_b = generate_matrix_data()

    matrix_add = matrix_a + matrix_b
    matrix_mul = matrix_a * matrix_b
    matrix_matmul = matrix_a @ matrix_b

    save_matrices(matrix_a, matrix_b, matrix_add, matrix_mul, matrix_matmul, task_number="3.1")


def task_3_2():
    matrix_a, matrix_b = generate_matrix_data()

    matrix_add = matrix_a + matrix_b
    matrix_mul = matrix_a * matrix_b
    matrix_matmul = matrix_a @ matrix_b

    save_matrices(matrix_a, matrix_b, matrix_add, matrix_mul, matrix_matmul, task_number="3.2")

    print(matrix_a)


def main():
    task_3_1()
    task_3_2()


if __name__ == "__main__":
    main()

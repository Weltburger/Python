import numpy as np
from functools import reduce
from operator import mul


def _1():
    A = np.random.randint(0, 100, (3, 5))
    B = np.random.randint(0, 100, (5, 2))
    print(f'\n\nA = \n{A}\nB = {B}\nA * B = \n{A.dot(B)}')


def _2():
    A = np.random.randint(0, 100, (5, 3))
    B = np.random.random((3, 3, 3))
    print(f'\n\nA = \n{A}\nB = {B}\nA * B = \n{A.dot(B)}')


def _3():
    n = np.random.randint(0, 100)
    A = np.random.randint(0, 100, (n, n))
    B = np.random.randint(0, 100, (n))
    X = np.linalg.solve(A, B)
    print(f'\n\nA = \n{A}\n B = \n{B}\nX = \n{X}')


def _4():
    n = np.random.randint(1, 10)
    A = np.array(np.random.randint(0, 100, (n, n)))
    print(f'\n\nA = \n{A}\ndet(A) = \n{int(np.linalg.det(A))}')


def _5():
    n = np.random.randint(3, 4)
    A = np.array(np.random.randint(0, 100, (n, n)))
    print(f'\n\nA = \n{A}\nA^-1 = \n{np.linalg.inv(A)}\nA^T = \n{np.transpose(A)}')


def _5_1():
    not_equal_counter = 0
    iter_count = 1000
    for i in range(iter_count):
        A = np.array(np.random.randint(0, 100, (5, 5)))
        det = np.round(np.linalg.det(A))
        eigvals = np.round(reduce(mul, np.linalg.eigvals(A)))
        if not np.equal(det, eigvals):
            print(f'Not equal with det = {det} and eigvals = {eigvals}')
            not_equal_counter += 1
    print(f'\n\nWasn\'t equal {not_equal_counter} times of {iter_count} times')


if __name__ == '__main__':
    _1()
    _2()
    _3()
    _4()
    _5()
    _5_1()
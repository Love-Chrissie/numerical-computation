#!/usr/bin/env python3
# encoding: utf-8  

""" 
@version: v1.0 
@author: 四月是你的谎言
@contact: 389641222@qq.com 
@site:  
@software: PyCharm 
@file: chollt
@time: 2018/10/12 4:04 PM 
"""
import time
import numpy as np


def chollt(A):
    EPSILON = 1e-8
    DIM = len(A)
    for k in range(DIM):
        for i in range(k, DIM):
            for j in range(k):
                A[i, k] = A[i, k] - A[i, j] * A[k, j]
        if np.fabs(A[k, k]) < EPSILON:
            return 1
        A[k, k] = np.math.sqrt(A[k, k])
        for i in range(k+1, DIM):
            A[i, k] = A[i, k] / A[k, k]
    return 0


def trillt(A, x):
    EPSILON = 1e-8
    DIM = len(x)
    for i in range(DIM):
        for j in range(i):
            x[i] -= A[i, j] * x[j]
        if np.fabs(A[i, i]) < EPSILON:
            return 1
        else:
            x[i] /= A[i, i]
    for i in range(DIM-1, -1, -1):
        for j in range(i+1, DIM):
            x[i] -= A[j, i] * x[j]
        x[i] /= A[i, i]
    return 0


def main():
    A = np.array([[4.0, 1.0, 0.0],
                  [1.0, 5.0, 2.0],
                  [0.0, 2.0, 8.0]])
    b = np.array([5.0, 8.0, 10.0])
    DIM = len(b)
    start = time.process_time()
    chollt(A)
    trillt(A, b)
    end = time.process_time()
    print("The program use %f ms" % ((end - start) * 1000))
    print("Cholesky LLt decompsition:")
    for i in range(DIM):
        for j in range(i+1):
            print("{:12.8f}".format(A[i, j]), end = '')
        print("")
    print("The solution is:")
    for i in range(DIM):
        print("{:12.7f}".format(b[i]))



if __name__ == "__main__":
    main()

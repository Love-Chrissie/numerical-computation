#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 四月是你的谎言
@contact: 389641222@qq.com 
@site:  
@software: PyCharm 
@file: gcpelim
@time: 2018/10/11 9:31 AM 
"""
import time
import numpy as np


def gcpelim(process, A, xx):
    EPSILON = 1e-8
    DIM = len(xx)
    if(process == 1):
        print("The process of elimination:")
    for k in range(DIM):
        pelement = np.fabs(A[k, k])
        i0 = k
        for i in range(k, DIM):
            if np.fabs(A[i, k]) > pelement:
                pelement = np.fabs(A[i, k])
                i0 = i
        if i0 != k:
            for j in range(DIM):
                pelement = A[k, j]
                A[k, j] = A[i0, j]
                A[i0, j] = pelement
            pelement = xx[k]
            xx[k] = xx[i0]
            xx[i0] = pelement
        if np.fabs(A[k, k]) < EPSILON:
            return 1
        for i in range(k+1, DIM):
            A[i, k] = A[i, k]/A[k, k]
            for j in range(k+1, DIM):
                A[i, j] = A[i, j]-A[i, k]*A[k, j]
            xx[i] = xx[i]-A[i, k]*xx[k]
        if process == 1:
            for i in range(DIM):
                for j in range(DIM):
                    print("{:10.6f}\t".format(A[i, j]), end="")
                print("{:10.6f}".format(xx[i]))
            print('')
    for i in range(DIM-1, -1, -1):
        for j in range(i+1, DIM):
            xx[i] = xx[i] - A[i, j]*xx[j]
        xx[i] = xx[i]/A[i, i]
    return 0


def getMatrix(n):
    A = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = 1/(i+j+1)
    return A


def main():
    n = int(input("请输入计算向量大小："))
    A = getMatrix(n)
    xx = np.ones(n)
    start = time.process_time()
    gcpelim(1, A, xx)
    end = time.process_time()
    print("Column principle elimination for the solution:")
    for x in xx:
        print("{:10.6f}".format(x))
    print("The program use %f ms" % ((end - start)*1000))


if __name__ == "__main__":
    main()

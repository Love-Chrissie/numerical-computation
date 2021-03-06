这是我数值计算学习过程中编写的一些代码，也在[博客](https://love-chrissie.github.io/)中有一定的介绍。

### 目录

- 求解一般线性方程组的[高斯消去法](gelim.c)与[高斯列主元消去法](gcpelim.py)

- 高斯消去法引出的[LU分解](LU.py)

- 针对系数矩阵为正定对称矩阵的[楚斯基(Cholesky)分解](chollt.py)

- 针对系数矩阵为三对角矩阵的[追赶法(托马斯算法)](thomas.py)，这种类型的线性方程组求解在实际中经常遇到。

- 求解一般线性方程组的[迭代法](迭代法/iterativeMethod.cpp)，包括雅可比迭代、高斯塞德尔迭代和连续过松弛迭代。

- 针对系数矩阵为正定对称矩阵的迭代法：[共轭梯度法](迭代法/ConjugateGradient.py)

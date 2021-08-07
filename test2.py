#!/usr/bin/env python3
# importのテスト

import numpy as np

# 配列の生成
arr1 = np.array([[0, 1, 2], [3, 4, 5]])
print(arr1)

# 等差数列
arr2 = np.arange(6)
print(arr2)

# 行列(二次元配列)
mat = np.matrix([[0, 1, 2], [3, 4, 5]])
print(mat)

mat2 = np.matrix(arr1)
print(mat2)

# 行列の要素の取得
print(mat[0, 1])

mat[0, 1] = 100
print(mat)









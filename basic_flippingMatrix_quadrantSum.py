#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [14, 8, 7, 6], [11, 12, 13, 9], [15, 16, 17, 18]]
    for r in matrix:
        print(r)
    n = int(len(matrix) / 2)
    max_sum = 0
    for iq in range(n):
        for jq in range(n):
            pos1 = matrix[iq][jq]
            pos2 = matrix[iq][(2 * n - 1) - jq]
            pos3 = matrix[(2 * n - 1) - iq][jq]
            pos4 = matrix[(2 * n - 1) - iq][(2 * n - 1) - jq]
            # print(pos1, pos2, pos3, pos4)
            # print(max([pos1, pos2, pos3, pos4]))
            max_sum += max([pos1, pos2, pos3, pos4])
    print(max_sum)

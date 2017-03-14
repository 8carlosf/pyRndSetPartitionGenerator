#!/usr/bin/env python3

from random import random, randint
from math import factorial, e

unm = lambda n, m, b: ((m**n)/(factorial(m)*b))/e

def genBellNumbers(n):
    B = [0]*(n+1) # Bell Numbers
    S = [[0]*(n+1) for i in range(n+1)] # Stirling numbers of the second kind
    S[0][1] = 1
    B[0] = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            S[i][j] = S[i-1][j]*j + S[i-1][j-1]
            B[i] += S[i][j]
        S[i-1] = [] # clean Stirling numbers (ram management)
    return B

def getBellNumber(n):
    B = genBellNumbers(n)
    return B[n]

def getM(n, b):
    p = random()
    m = 0
    while(p > 0):
        p -= unm(n, m, b)
        m += 1
    return m

# 1 - choose M from unm (getM)
# 2 - Drop n labelled balls uniformly into M boxes
# 3 - Form a set partition λ of [n] with i and j in the same block if and only if balls i and j are in the same box
def getRandomSet(n, b):
    m = getM(n, b)
    b = []
    for i in range(n):
        b += [randint(0, m-1)]
    
    norm = [-1]*m
    normC = 0
    for i in range(n):
        if norm[b[i]] < 0:
            norm[b[i]] = normC
            normC += 1
        b[i] = norm[b[i]]

    return b

if __name__ == "__main__":
    print(genBellNumbers(10))
    for i in range(1000):
        b = getBellNumber(3)
        print(' '.join(map(str, getRandomSet(3, b))))

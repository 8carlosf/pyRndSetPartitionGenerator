#!/usr/bin/env python3

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

if __name__ == "__main__":
    print(genBellNumbers(10))
    print(getBellNumber(10))

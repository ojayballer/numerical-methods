"""
======================================================================
LU Decomposition Solver using Doolittle's Method
----------------------------------------------------------------------

Overview:
---------
This script solves a system of linear equations Ax = B using
LU decomposition with Doolittle's method.

Doolittle's algorithm factors matrix A into:
    A = L * U  
Where:
    - L is a lower triangular matrix with unit diagonal (1s on the diagonal)
    - U is an upper triangular matrix

The system is solved in two steps:
1. Forward substitution to solve Ly = B
2. Backward substitution to solve Ux = y

What It Does:
-------------
✔ Performs LU decomposition without pivoting  
✔ Solves a 4x4 system Ax = B using the LU factorization  
✔ Returns and prints the L, U matrices and solution vector x

Functions():
----------------
1. doolittle_LU_decomposition(n, A):
    Decomposes square matrix A into L and U using Doolittle’s method.

2. forward_substitution(L, B, n):
    Solves the intermediate system Ly = B.

3. backward_substitution(U, y, n):
    Solves the upper-triangular system Ux = y.

4. test():
    Defines a 4x4 matrix A and right-hand-side vector B,
    then applies LU decomposition and solves for x.


Expected output includes:
- The L and U matrices from decomposition
- The solution vector x for the system Ax = B

Notes:
------
- This implementation does not use partial pivoting. It works best
  for well-conditioned systems where pivoting isn't required.
- Ideal for educational purposes or small systems (e.g., 2x2 to 5x5)

======================================================================
"""



import numpy as np
def doolittle_LU_decomposition(n,A):

    L=np.zeros((n,n))
    for i in range(0,n):
      for j in range(0,n):
        if i==j:
           L[i][j]=1
    U=np.zeros((n,n))
    
    for  k in range(n):
        #fills U
        for j in range(k,n):
          c=0
          for s in range(k):
            c+= L[k][s]*U[s][j]
          U[k][j]=A[k][j]-c
          
        #fills L
        for i in range(k+1,n):
            p=0
            for s in range(k):
              p+=L[i][s]*U[s][k]
            L[i][k]=(A[i][k]-p)/U[k][k]
            
    return L,U
    
def forward_substitution(L,B,n):
    y=[0]*n
    
    for i in  range(0,n):
        sum=0
        for j in range(i):
            sum+=L[i][j]*y[j]
        y[i]=B[i]-sum
    return y

def backward_substitution(U,y,n):
    x=[0]*n
    for i in range(n-1,-1,-1):
        v=0
        for j in range(i+1,n):
            v+=(U[i][j]*x[j])
        x[i]=(y[i]-v)/U[i][i]
    return x
                    
def test(): 
   n=4
   A=np.array([
    [1,-1,3,2],
    [1,5,-5,-2],
    [3,-5,19,3],
     [2,-2,3,21] ])
   
   B=np.array([15,-35,94,1])
   
   L,U=doolittle_LU_decomposition(n,A)
   y=forward_substitution(L,B,n)
   x=backward_substitution(U,y,n)
   x=[float(i) for i in x]
   print(f"L:{L}\n\n U:{U}\n")
   print(f"solution vector x:{x}" )

test()
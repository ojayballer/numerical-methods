"""
Thomas Algorithm for Tridiagonal Systems
----------------------------------------

This Python function implements the **Thomas Algorithm**, an efficient method 
to solve tridiagonal linear systems of equations. It is especially useful for 
numerical applications such as **natural cubic spline interpolation**.

Function:
---------
- thomas_algorithm(x, y):
    Solves a tridiagonal system derived from the natural cubic spline formulation
    and returns the second derivatives (M values) at each data point.

Parameters:
-----------
- x : list of float
    List of strictly increasing x-values (independent variable).
- y : list of float
    Corresponding y-values (dependent variable).

Returns:
--------
- M : list of float
    List of second derivatives at each x-value (spline coefficients), where
    M[0] and M[-1] are 0 due to natural spline boundary conditions.

Steps:
------
1. Compute interval widths h
2. Form coefficient vectors a, b, c and right-hand side vector d
3. Perform forward elimination
4. Perform backward substitution to obtain M

Usage:
------
Use this function within a cubic spline interpolation module to compute 
the second derivatives needed for spline segment equations.

Example:
--------
    M = thomas_algorithm(x, y)

Notes:
------
- Assumes natural spline conditions: M[0] = M[n] = 0
- Input x must be strictly increasing
- Only supports interpolation (not extrapolation)


"""

def thomas_algorithm(x,y):
    n=len(x)
    h=[x[i+1]-x[i] for i in range(n-1)]
    a=[0]*(n-2)
    b=[0]*(n-1)
    c=[0]*(n-2)
    d=[0]*(n-1)
    M=[0]*(n)
    M[0]=0
    M[-1]=0
    for  i in range(1,n-1):
        a[i-1]=h[i-1]/6.0
        b[i]=(h[i-1]+h[i])/3.0
        c[i-1]=h[i]/6.0
        d[i-1]=(y[i+1]-y[i])/h[i]-(y[i]-y[i-1])/h[i-1]
    
    for i in range(2,n-1):#Forward elimination
        r=a[i-1]/b[i-1]
        b[i]-=r*c[i-2]
        d[i-1]-=r*d[i-2]
        
    M[n-2] = d[n-3] / b[n-2] 
    
    for i in range(n-3,0,-1):#backward substitution
        M[i]=(d[i-1]-c[i-1]*M[i+1])/b[i]
        
    return M

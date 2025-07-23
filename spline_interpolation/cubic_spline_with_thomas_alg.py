"""
===========================================================================
Cubic Spline Interpolation using Thomas Algorithm (Natural Boundary)
---------------------------------------------------------------------------

Overview:
---------
This script performs **natural cubic spline interpolation** on a set of 
data points using a custom-built tridiagonal solver (Thomas Algorithm).  
It evaluates the smooth spline curve at desired query points and 
visualizes both the original data and interpolated curve.

What It Does:
-------------
Solves the tridiagonal system for second derivatives (M values)  
Computes cubic spline segments between each pair of known points  
Evaluates and plots the spline over a fine grid  
Uses natural boundary conditions (second derivatives at ends = 0)

Functions():
----------------
1. thomas_algorithm(x, y):
   - Constructs and solves the tridiagonal system to compute 
     second derivatives of the spline.
   - Returns the list of M values (curvature at each x).

2. my_cubic_spline_flat(x, y, X):
   - Takes known data points `(x, y)` and query points `X`
   - Uses cubic spline interpolation to compute interpolated values `Y`

3. visualize_data(x, y, X, Y):
   - Plots the original data points and the smooth spline curve

4. test_case():
   - Defines a sample dataset
   - Interpolates values on a fine interval using the spline
   - Visualizes the result and returns interpolated `Y`

5. main():
   - Entry point that runs the full test and displays output

You'll see a smooth red curve passing through black circular data points, 
representing the cubic spline interpolation.

Notes:
------
- This implementation uses **natural boundary conditions**, meaning:
      M₀ = Mₙ = 0
- The Thomas algorithm is used for efficient solving of the tridiagonal system.
- The method is ideal for smoothly interpolating physical or tabulated data
  (e.g., engineering or physics applications).

===========================================================================
"""



import numpy as np
import matplotlib.pyplot as plt
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

def my_cubic_spline_flat(x,y,X):
   M=thomas_algorithm(x,y)
   n=len(x)
   h=[x[i+1]-x[i] for i in range(n-1)]
   
   Y=[]
   for query in X:
      if  query< x[0] or query>x[-1]:
         raise ValueError("x_query is out of interpolation range")
   
   for query in X:
     for i in range(n-1):
        if query>=x[i] and  query<=x[i+1]:
                A = x[i+1] - query
                B = query - x[i]
                S = (M[i] * A**3 + M[i+1] * B**3) /(6 * h[i]) \
                    + (y[i] / h[i] - (M[i] * h[i]) / 6) * A \
                      + (y[i+1] / h[i] - (M[i+1] * h[i]) / 6) * B
                Y.append(S)
                break
     else:
            raise ValueError("no interval found for x_query")
     
   return Y

def visualize_data(x,y,X,Y):
    plt.plot(x,y,'ko',label='Data points')
    plt.plot(X,Y,'r-',label="cubic spline")
    plt.title("cubic spline interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.show()

    
def test_case():
   x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0 , 1.2,
        1.4, 1.6 , 1.8, 2.0 , 2.2, 2.4, 2.6,
        2.8]
   
   y = [10.0, 11.216, 11.728, 11.632, 11.024,
        10.0, 8.656, 7.088, 5.392, 3.664, 
        2.0 , 0.496, -0.752, -1.648, -2.096]
   
   X = np.linspace(x[0], x[-1], 100)
    
   Y=my_cubic_spline_flat(x,y,X)
   Y=[float(i) for i in Y ]
   visualize_data(x,y,X,Y)
   return f"Y: {Y}"


def main():
   print(test_case())
    
if __name__=="__main__":
    main()
    


       
   
        
    
        
   
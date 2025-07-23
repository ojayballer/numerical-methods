"""
Natural Cubic Spline Interpolation in Python 

This script builds a natural cubic spline interpolator from scratch using SymPy.
It's a symbolic (non-numeric) implementation, meaning it builds and solves the
system of equations for the spline coefficients exactly — no matrix libraries needed.


 What does it do?

Given some known data points (x, y), it:
- Constructs a cubic spline that smoothly passes through all the points.
- Enforces natural boundary conditions (zero second derivative at the endpoints).
- Evaluates the spline at custom query points X (any points between x[0] and x[-1]).
- Plots both the original points and the resulting smooth curve.

How does it work?

For each interval between two data points, we define a cubic polynomial:

    Sᵢ(x) = aᵢ + bᵢ(x - xᵢ) + cᵢ(x - xᵢ)² + dᵢ(x - xᵢ)³

Then we generate equations to make sure:
- The function hits the correct y-values at endpoints.
- The first and second derivatives match at the joins.
- The spline is "natural", meaning its second derivative is zero at the first and last x.

All equations are symbolically solved using sympy.solve().


How to use:

- Define your data points x and y
- Choose your query points X (must lie inside the range of x)
- Call my_cubic_spline_flat(x, y, X) to get interpolated y-values
- Use visualize_data(x, y, X, Y) to plot everything

You can run the script directly — it includes a test_case() to show how it works.

Requirements:
- sympy
- matplotlib
- numpy

Install them using:
    pip install sympy matplotlib numpy
"""
from sympy import Eq,solve,symbols
import numpy as np
import matplotlib.pyplot as plt
from sympy import Rational
def my_cubic_spline_flat(x,y,X):
    n=len(x)-1
    a = symbols(f'a0:{n}') 
    b=symbols(f"b0:{n}")    #bo,b1,...,bn-1
    c=symbols(f"c0:{n}")    #co,c1,....,cn-1
    d=symbols(f"d0:{n}")    #do,d1,.....,dn-1
        
    for query in X: 
     if query<x[0] or query>x[-1]:
        raise ValueError("x_query is out of the interpolation range")
   
    
    equations=[]
    
    for i in range(n):
        eq=Eq(a[i],y[i])
        equations.append(eq)
        eq=Eq(a[i]+b[i]*(x[i+1]-x[i])+c[i]*(x[i+1]-x[i])**2+d[i]*(x[i+1]-x[i])**3,y[i+1])
        equations.append(eq)
        
    for i in range(n-1):
        eq=Eq(b[i]+2*c[i]*(x[i+1]-x[i])+3*d[i]*(x[i+1]-x[i])**2,b[i+1])#first continuity equation
        equations.append(eq)
        
        eq=Eq(2*c[i]+6*d[i]*(x[i+1]-x[i]),2*c[i+1])#second continuity equation
        equations.append(eq)
       
    #boundary conditions
    eq=Eq(c[0],0)
    equations.append(eq)
    eq=Eq(2*c[-1]+6*d[-1]*(x[-1]-x[-2]),0)
    equations.append(eq)
    
    solution=solve(equations)
    
    Y=[]
    for query in X:
       for i in range(n):
          xi=x[i]
          xi1=x[i+1]
          if query>=xi and query<=xi1:
             h=query-xi
             ai=solution[a[i]]
             bi=solution[b[i]]
             ci=solution[c[i]]
             di=solution[d[i]]
             Y.append(float(ai+bi*h+ci*h**2+di*h**3))
             break
       else:     
         raise ValueError("interpolation interval was not found for x_query")
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
   x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0 , 1.2, 1.4, 1.6
                                   , 1.8, 2.0 , 2.2, 2.4, 2.6,
                                   2.8]
   
   y = [10.0, 11.216, 11.728, 11.632, 11.024, 
                                   10.0, 8.656, 
                                   7.088, 5.392, 3.664, 
                                   2.0 , 0.496, -0.752, -1.648, -2.096]
   
   X = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 
                                   1.3, 1.5, 1.7, 1.9, 2.1, 2.3,
                                   2.5, 2.7]

    
   Y=my_cubic_spline_flat(x,y,X)
   visualize_data(x,y,X,Y)
   return Y
def main():
   print(test_case())
    
if __name__=="__main__":
    main()
    

    
    
    
        
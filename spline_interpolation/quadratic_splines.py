"""
Quadratic Spline Interpolation 

 Overview:
This script performs **quadratic spline interpolation** using symbolic computation with SymPy. It builds a system of equations to fit a smooth curve through given data points, while maintaining slope continuity and satisfying boundary conditions.

What Are Quadratic Splines?
Quadratic splines are piecewise second-degree polynomials:
    Sᵢ(x) = aᵢ + bᵢ(x - xᵢ) + cᵢ(x - xᵢ)²

They ensure:
- Each spline passes through two consecutive data points
- The first derivatives (slopes) match at internal points
- A simple boundary condition (c₀ = 0) helps uniquely define the curve

What This Script Does:
- Symbolically constructs spline equations for all intervals
- Automatically solves the system using SymPy
- Evaluates interpolated values at any query points
- Visualizes the data, interpolated curve, and smooth transitions using Matplotlib

Features:
- Educational and transparent spline construction
- Continuity of the first derivative for a smooth curve
- Precise and symbolic solution (great for learning)
- Clear visual representation of both raw and interpolated data
- Handles interpolation domain errors correctly

"""
from sympy import symbols,Eq, solve
import matplotlib.pyplot as plt
import numpy as np
def quadratic_spline(x,y,x_query): 
   n=len(x)-1#  n segments
   b=symbols(f"b0:{n}")
   c=symbols(f"c0:{n}")
   
   for query in x_query: 
     if query<x[0] or query>x[-1]:
        raise ValueError("x_query is out of the interpolation range")
    
   y_query=[]
   equations=[]
   a=[y[i] for i in range(n)]  
   
   for i in range(n):#interpolation condition
       xi=x[i]
       xi1=x[i+1]
       h=xi1-xi
       eq=Eq(a[i]+b[i]*h+c[i]*h**2,y[i+1])
       equations.append(eq)
       
   for i in range(n-1):#first continuity equation
       h=x[i+1]-x[i]
       eq=Eq(b[i]+2*c[i]*h,b[i+1])
       equations.append(eq)
       
#boundary condition 
   equations.append(Eq(c[0],0))
   solution=solve(equations)
   
   #Evaluate spline at x_query
   
   for query in x_query:
      for i in range(n):
          xi=x[i]
          xi1=x[i+1]
          if query>=xi and query<=xi1:
             h=query-xi
             ai=a[i]
             bi=solution[b[i]]
             ci=solution[c[i]]
             y_query.append(float(ai+bi*h+ci*h**2))
             break
      else:     
         raise ValueError("interpolation interval was not found for x_query")
   return y_query

def visualize(x,y,x_query,y_query):
    plt.title("Quadratic Spline Interpolation")
    plt.plot(x,y,'ko',label='Data points')
    plt.plot(x_query,y_query,'r-',label="interpolated point")
   
    plt.xlabel("x")
    plt.ylabel("y")
   
    plt.grid()
    plt.legend()
    plt.show()

def test_case():
    x=[0.0,
        0.2,
        0.4,
        0.6,
        0.8,
        1.0,
        1.2,
        1.4,
        1.6,
        1.8,
        2.0,
        2.2,
        2.4,
        2.6,
        2.8,]
    y=[ 10.0,
        11.216,
        11.728,
        11.632,
        11.024,
        10.0,
        8.656,
        7.088,
        5.392,
        3.664,
        2.0,
        0.496,
        -0.752,
        -1.648,
        -2.096,]
    x_query=[0.0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18,
        0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38,
        0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58,
        0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78,
        0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98,
        1.0, 1.02, 1.04, 1.06, 1.08, 1.1, 1.12, 1.14, 1.16, 1.18,
        1.2, 1.22, 1.24, 1.26, 1.28, 1.3, 1.32, 1.34, 1.36, 1.38,
        1.4, 1.42, 1.44, 1.46, 1.48, 1.5, 1.52, 1.54, 1.56, 1.58,
        1.6, 1.62, 1.64, 1.66, 1.68, 1.7, 1.72, 1.74, 1.76, 1.78,
        1.8, 1.82, 1.84, 1.86, 1.88, 1.9, 1.92, 1.94, 1.96, 1.98,
        2.0, 2.02, 2.04, 2.06, 2.08, 2.1, 2.12, 2.14, 2.16, 2.18,
        2.2, 2.22, 2.24, 2.26, 2.28, 2.3, 2.32, 2.34, 2.36, 2.38,
        2.4, 2.42, 2.44, 2.46, 2.48, 2.5, 2.52, 2.54, 2.56, 2.58,
        2.6, 2.62, 2.64, 2.66, 2.68, 2.7, 2.72, 2.74, 2.76, 2.78,
        2.8]
    y_query=quadratic_spline(x,y,x_query)
    visualize(x,y,x_query,y_query)
    return y_query


def main():
    results=test_case()
    print(results)
    
if __name__ == "__main__":
    main()

      

    
           
           
           
   
       
       
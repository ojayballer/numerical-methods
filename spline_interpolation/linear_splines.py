import numpy as np
import matplotlib.pyplot as plt
"""
Linear Spline Interpolation 
Concept:
Linear spline interpolation connects each pair of known data points (x_i, y_i) and (x_{i+1}, y_{i+1}) 
with a straight line. This results in a piecewise linear function — one straight line per interval.
It's simple, efficient, and useful when you only need continuity (not smoothness of derivatives).

Each interval [x_i, x_{i+1}] is approximated with the formula:
    s_i(x) = y_i + m_i * (x - x_i), where m_i = (y_{i+1} - y_i) / (x_{i+1} - x_i)

 What this code does:
- Accepts known data points as arrays x and y
- Takes oneor multiple x_query values
- For the x_query(s),it locates the interval it falls in
- Computes the corresponding y_query value using linear interpolation
- Plots the original points and the interpolated point(s)

Variables:
- x, y         → known data points (must be sorted in increasing x)
- x_query      → the value(s) at which you want to estimate y
- xo, x1       → the endpoints of the interval that contains x_query
- yo, y1     → corresponding y-values at xo and x1
- m             → the slope between (xo, yo) and (x1, y1)
-y_result       stores  y_query  and y_query in return stores the → interpolated
                                               results at x_query

Supports:
- single or multiple queries: e.g., x_query =[2, 5,4..]

visualization:
Includes a visualize() function to plot:
- Original data points (black + markers)
- Interpolated point (red circles)

I Designed it to be clear, educational, and easy to modify.


    """

def linear_interpolation(x,y,x_query):
  y_result=[]
  n=len(x)
  for query in x_query:
    if query<x[0] or query>x[-1]:
        raise ValueError("x_query is out of the interpolation range")
    
    for i in range(n-1):
        xo=x[i]
        x1=x[i+1]
        if query>=xo and query<=x1:
          yo=y[i]
          y1=y[i+1]
       
          m=(y1-yo)/(x1-xo)
          g=query-xo
          y_query=m*g+yo
          y_result.append(y_query)
          break
  return y_result
    
   
def visualize(x,y,x_query,y_result):
    plt.plot(x,y,'ko',label="Data points")
    plt.plot(x_query,y_result,'r-',label="interpolated point")
    plt.title("Linear Spline Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.show()
    

def test_case():
    x= [
        0.0,
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
        2.8,
    ]
    y= [
        10.0,
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
        -2.096,
    ]
    x_query=[
        0.0,
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
        2.8,
    ]
    y_result=(linear_interpolation(x,y,x_query))
    print(y_result)
    visualize(x,y,x_query,y_result)
    

   
def main():
     test_case()
       
   
if __name__=="__main__":
    main()
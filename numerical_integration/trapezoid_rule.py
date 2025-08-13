'''# Trapezoidal Rule Python Script

## Description
This Python script approximates the definite integral of a given function over a specified interval
using the **Trapezoidal Rule**, a numerical integration method. 
The function can be passed as a string, allowing flexible evaluation.

## Features
- Accepts any mathematical function of x (as a string) that Python can evaluate.
- Works for any interval [a, b] and number of subintervals n.
- Calculates the step size automatically.
- Sums function values at interior points using the trapezoidal formula.

## Usage

1. Import the function or copy the script into your project.
2. Call the function with the following parameters:

```python
trapezoidal_rule(a, b, n, func)
  '''

def trapezoidal_rule(a,b,n,func):
    h=(b-a)/n
    part_sum=0
    def f(x):
        f=eval(func)
        return f
    for i in range(1,n):
        part_sum+=f(a+i*h)
    sum=f(a)+f(b)+2*part_sum
    approx_integral=(h/2)*sum
    return f"approx_integral of the function {func} with boundary {[a,b]} is {approx_integral}"
#Example case
print(trapezoidal_rule(0,1,8,"4/(1+x**(2))"))

    

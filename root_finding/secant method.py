'''Secant Method Root Finder
This Python script implements the Secant Method, a numerical technique used to approximate the roots of a real-valued function without requiring its derivative.

📌 Features
Finds an approximate root of any valid mathematical function (given as a string).

Uses the secant iteration formula for root-finding.

Stops early if the root estimate change is below 1e-6 tolerance.

Formats the result to 4 decimal places.

🧮 Method Overview
The Secant Method is an iterative process that updates guesses of the root using:
x_{n+1} = x_n - f(x_n) * ( (x_n - x_{n-1}) / ( f(x_n) - f(x_{n-1}) ) )'''

def secant_method(xo,xi,n,func):
    def f(x):
        f=eval(func)
        return f
    for i in range(n):
        X1=xo-f(xo)*((xo-xi)/(f(xo)-f(xi)))
        if abs(X1-xo)<1e-6:
            print(f"breaking.......... now at iteration {i}")
            break
        xi=xo
        xo=X1
      
    return f"A root of the function {func} has been found and it has a value of {X1:.4f}"
#example case
print(secant_method(3,2,6,"x**(3)-2*(x)-5"))

            

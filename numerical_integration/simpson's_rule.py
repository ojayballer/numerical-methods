'''This Python script approximates the definite integral of a given function over a specified interval
using Simpson’s Rule, a numerical integration method that is more accurate than the trapezoidal rule
for the same number of subintervals.

Important: The number of subintervals n must be even.

Features
Accepts any mathematical function of x (as a string) that Python can evaluate.

Checks that n is even and raises a ValueError if not.

Calculates the step size automatically.

Applies the Simpson’s rule formula with proper weighting of points (4 and 2).'''

def simpsons_rule(a,b,n,func):
   if n%2!=0:
       raise ValueError("Please enter an even number as n") 
   
   h=(b-a)/n
   def f(x):
       f=eval(func)
       return f
   S=f(a)+f(b)
   for i in range(1,n):
       
       if i%2==0: 
           d=2*f(a+i*h)
           S+=d
     
       if i%2!=0:
           d=4*f(a+i*h)
           S+=d
   approx_integral=h/3*(S) 
   return f"approx_integral of the function {func} with boundary {[a,b]} is {approx_integral}"
#example case
simpsons_rule(0,1,8,"4/(1+x**(2))")
  

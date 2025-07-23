import math
"""
Bisection Method (from scratch)

Concept:
The Bisection Method is a reliable root-finding algorithm that requires a continuous function f(x)
on an interval [a, b] where the function changes sign (i.e., f(a) * f(b) < 0). It repeatedly bisects the interval 
and chooses the subinterval where the sign change occurs — ensuring convergence toward the root.

At each step:
    - Compute midpoint: c = (a + b) / 2
    - If f(c) is close to zero (within tolerance), return c as the root
    - Else:
         If f(a) * f(c) > 0 → the root lies in [c, b] → set a = c
         Else               → the root lies in [a, c] → set b = c

 Parameters:
- func: A string representation of the function f(x), e.g., "x**3 - 2*x - 5"
- a, b: The initial interval endpoints (must satisfy f(a) * f(b) < 0)
- n: Maximum number of iterations (default is 30)

 Output:
- If no sign change is found, it tells the user to "Try again"
- If f(a) or f(b) is exactly zero, it declares a root at the endpoint
- If valid, it prints:
    - The function string
    - The root found (within tolerance)
    - Number of iterations used

 Algorithm Variables:
- a, b: The bracketing interval for the root
- c: Midpoint of the current interval
- f(x): Evaluated using eval(func) inside a local f() helper
- i: Iteration counter

Notes:
- The function uses eval() and assumes math is imported for expressions like math.exp(x)
- You must manually verify that f(a) * f(b) < 0 — or else it won't proceed

Designed for educational purposes: clean, minimal, and transparent.
"""

def bisection_method(func,a,b,n=30):
  def f(x):
       f=eval(func)
       return f
  if f(a)*f(b)>0:
       print("Try again man,you got this!")
  elif f(a)==0:
       print(f"The root of {func} is {a}")
  elif f(b)==0:
       print(f"The root of {func} is {b}")
  else:
       print("you are on the right track man,you can do this") 
       i=1
       while(i<=n):
          c=(a+b)/2
          i+=1
          if abs(f(c))<1e-6:
             break
          if f(a)*f(c)>0:#means f(c) is positive 
             a=c
          else:
             b=c
       print(f"The root of {func} is {c} in {i} iterations")
#example cases
bisection_method("2*(x)**2-7*(x)+6",1.5,2.5,10)
print()
bisection_method("x**(2)+x-6",-4,-2,10)
bisection_method("1 - 2*x*math.exp(-x/2)",0,1,12)
print()
bisection_method("5-(x)**(-1)",0.1,1)
print()
bisection_method("x**(3)-2*(x)-5",2,3)
print()
bisection_method("math.exp(x)-2",0,1)
print()
bisection_method("x-math.exp(-x)",0,1)
print()
bisection_method("x**(6)-x-1",1,2,)
print()
bisection_method("x**(2)-math.sin(x)",0.5,1)
print()
bisection_method("x**(3)-2",1,2)
print()
bisection_method("x+math.tan(x)",-1,0)
print()
#bisection_method("2-((x)**(-1)*math.log(x))",0.33,10)#bisection will not work here,no [-ve,+ve] interval







import math
def newtons_method(func,func_derivative,x,n):   
    """
Newton-Raphson Method 

Concept:
Newton-Raphson is an iterative root-finding method that uses the tangent line at a current guess to 
approximate the root of a real-valued function. It converges quickly when starting near the actual root.

At each step, it applies:
    x_{n+1} = x_n - f(x_n)/f'(x_n)

What this code does:
- Takes a function func and its derivative func_derivative as strings
- Accepts an initial guess x and number of iterations n
- At each iteration:
    ▸ Evaluates f(x) and f'(x) using eval()
    ▸ Updates x using the Newton-Raphson formula
    ▸ Stops early if the change in x is smaller than a tolerance (1e-6)

 Parameters:
- func: A string representing the function f(x) (e.g. "x**3 - 2*x - 5")
- func_derivative: A string representing f'(x) (e.g. "3*x**2 - 2")
- x: Initial guess for the root
- n: Maximum number of iterations

 Output:
- Prints the function, derivative, final estimated root, and iteration count

 Algorithm variables:
- x: the current approximation of the root (updated every iteration)
- f(x): computed using eval(func) inside the f() function
- df(x): computed using eval(func_derivative) inside the df() function
- i: the updated root approximation each step (used to compare convergence)
- a: current iteration number (printed at the end)

 Notes:
- Assumes the function and derivative are correctly written with x and math if needed
- Does not handle division by zero explicitly
- Uses absolute error stopping condition: abs(i - x) < 1e-6

"""

    def f(x):
        f=eval(func)
        return f
    def df(x):
        df=eval(func_derivative)
        return df
    for a in range(1,n):
        i=x-(f(x)/df(x)) 
        if(abs(i-x)<1e-6):
           break
        x=i  
    print(f" f(x): {func}\n first derivative :{func_derivative}\n root:{x} \n iteration no: {a}")
   
#example functions
newtons_method("1 - 2*x*math.exp(-x/2)","-math.exp(-x/2)*(2 - x)",0,10)
print()
newtons_method("5-(x)**(-1)","x**(-2)",0.25,10)
print()
newtons_method("x**(3)-2*(x)-5","3*(x)**2-2",2,10)
print()
newtons_method("math.exp(x)-2","math.exp(x)",1,10)
print()
newtons_method("x-math.exp(-x)","1+math.exp(-x)",1,10)
print()
newtons_method("x**(6)-x-1","6*(x)**(5)-1",1,10)
print()
newtons_method("x**(2)-math.sin(x)","2*(x)-math.cos(x)",0.5,10)
print()
newtons_method("x**(3)-2","3*(x)**2",1,10)
print()
newtons_method("x+math.tan(x)","1+1/math.cos(x)**2",3,10)
print()
newtons_method("2-((x)**(-1)*math.log(x))","(1-math.log(x))/x**(2)",0.33,10)




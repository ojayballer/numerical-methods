import pandas as pd
def improved_eulers_method(func,Xo,Yo,n,h):
    """
     Improved Euler's Method (Heun's Method) — Step-by-step Table Generator

    Concept:
    This is a numerical method for solving first-order ordinary differential equations (ODEs) of the form:
        dy/dx = f(x, y)

    It improves upon Euler's method by using the **average slope** between:
    - The slope at the beginning of the interval, and
    - The slope at the predicted value at the end of the interval

    Formula:
        y_predict = y_n + h * f(x_n, y_n)
        y_{n+1} = y_n + (h/2) * [f(x_n, y_n) + f(x_n+h, y_predict)]

     Parameters:
    - func:      A string representing the function f(x, y), e.g., "X0 + Y0"
    - X0, Y0:     Initial values of x and y
    - n:          Number of steps/iterations
    - h:          Step size

     Output:
    - A formatted table (DataFrame converted to string) showing:
        [Iteration, x_n, y_n, Euler y_predict, Improved Euler y_{n+1}]

     Note:
    - The function uses eval(func) with X0 and Y0 as variable names.
    - Returns a string for clean printing in terminal or notebook.
    """


    
    
    def f(Xo,Yo):
        f=eval(func)
        return f 
    df=pd.DataFrame(columns=['__n__ ','  __Xn__ ','    __Yn__','    __y_pred(euler)__','    __Yn+1(improved euler__'])
    for i in range(0,n):
      y_pred=Yo+h*f(Xo,Yo)   
      Yn1=Yo+h*float((f(Xo,Yo)+f(Xo+h,y_pred))/2)
      df.loc[i]=[i,Xo,Yo,y_pred,Yn1]
      Xo=Xo+h
      Yo=Yn1
    return df.to_string(index=False)
    
 
#example case
table=improved_eulers_method("Xo+Yo",0.0,1,20,0.1)
print(table)  
        
"""
============================================================
Fast Fourier Transform (FFT) Visualizer
------------------------------------------------------------


Overview:
---------
This script performs a Fast Fourier Transform (FFT) on a 
discrete time-domain signal to analyze its frequency content.
It uses a recursive implementation of the Cooley-Tukey FFT 
algorithm, which significantly improves performance compared 
to the standard DFT.

What it does:
-------------
- Defines a sample signal of 20 evenly sampled values
- Applies FFT recursively (divide and conquer strategy)
- Extracts and plots the frequency magnitude spectrum
- Displays the result visually using matplotlib

Functions():
----------------
1. FFT(x):
    A recursive function that computes the FFT of a list `x`.

2. run_fft():
    Prepares a predefined signal and applies the FFT.

3. plot(x, X):
    Visualizes the frequency spectrum of the FFT result 
    (only half-spectrum shown since it’s symmetric for real signals).

4.`main():
    Entry point that calls the FFT and plotting routines.

How to Use:
-----------
Just run the script using Python:

    python fft_visualizer.py

You’ll see a stem plot showing the magnitudes of the frequency 
components of the input signal.

Notes:
------
- This implementation is for **educational purposes** and works 
  best with signals of length N = 2^k (power of two).
- The current signal has a sampling rate of 20 Hz and 20 points.
- The frequency spectrum is scaled by N to normalize the output.

============================================================
"""


import cmath
import time
import matplotlib.pyplot as plt 

def FFT(x):
    N=len(x)
    X=[0]*N
    
    if N>1:
      even=FFT(x[0::2])
      odd=FFT(x[1::2])

      for k in range(N//2):
          X[k]=even[k]+cmath.exp((-1j *2  *cmath.pi * k )/N)*odd[k]
          X[k+N//2]=even[k]-cmath.exp((-1j *2  *cmath.pi * k)/N)*odd[k]

      return X

    else:
        return x  
def run_fft():
    x = [ 0.00000000e+00, 
       5.57590997e+00, 2.04087031e+00, 
       -8.37717508e+00, -5.02028540e-01, 
       1.00000000e+01, -5.20431056e+00, 
       -7.68722952e-01, -5.56758182e+00,
       1.02781920e+01, 
       1.71450552e-15, -1.02781920e+01,
       5.56758182e+00, 7.68722952e-01, 
       5.20431056e+00, -1.00000000e+01,
       5.02028540e-01, 8.37717508e+00, 
       -2.04087031e+00, -5.57590997e+00]
    
    
    X = FFT(x)
    return x,X
 
def plot(x,X):
    N=len(x)
    sampling_time=[0., 0.05, 0.1 , 0.15, 0.2 , 0.25, 0.3 , 0.35, 
       0.4 , 0.45, 0.5 ,
       0.55, 0.6 , 0.65, 0.7 , 0.75, 0.8 ,
       0.85, 0.9 , 0.95]
    
    sampling_rate=20
      
    #plot the FFT magnitude spectrum
    f_k=[ k*sampling_rate/len(X)  for k in range(len(X))]  
    X_k=[abs(val)/N for val in X]
    plt.stem(f_k[:N//2], X_k[:N//2], basefmt=" ", label="FFT Magnitude(s)")
    plt.legend()
    plt.grid()
    plt.title("FAST FOURIER TRANSFORMS")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude(|X[k]|)")    
    plt.show()
    print(f"frequency_domain:{X} ")
    print(f"Magnitudes: {X_k} ")
    print(f"sampling time :{sampling_time}")
   
    
   
   
def main():
    x,X=run_fft()
    plot(x,X)

if __name__=="__main__":
    main()

 
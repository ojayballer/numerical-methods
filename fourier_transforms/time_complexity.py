"""
======================================================================
DFT vs FFT: Execution Time Comparison & Frequency Spectrum Visualizer
----------------------------------------------------------------------

Overview:
---------
This script compares the performance of the Discrete Fourier Transform (DFT)
and Fast Fourier Transform (FFT) on a predefined time-domain signal.

It uses:
- A manually implemented DFT from `discrete_fourier_transforms.py`
- A recursive Cooley-Tukey FFT implementation
- Python's `time` module to measure execution time
- `matplotlib` to plot the frequency magnitude spectrum

What It Does:
-------------
✔ Measures and prints execution time for both DFT (O(N²)) and FFT (O(N log N))  
✔ Computes and visualizes the FFT magnitude spectrum  
✔ Helps demonstrate why FFT is preferred in real-world signal processing

FUnctions()
----------------
1. FFT(x):
    A recursive function implementing the Cooley-Tukey FFT algorithm.

2. compare_time_complexity():
    - Loads a 20-point sample signal
    - Times the DFT and FFT computations
    - Prints out their respective execution durations

3. plot_fft(x, X):
    - Generates the magnitude spectrum from the FFT result
    - Plots it as a stem plot against frequency bins

4. main():
    Runs the time comparison and visualization functions.

How to Use:
-----------
Run the script with:

    python fft_vs_dft.py

You’ll get console output comparing DFT and FFT execution times,
and a plot showing the FFT frequency spectrum.

Notes:
------
- The signal is sampled at 20 Hz for a duration of 1 second.
- Only the FFT result is plotted (not the DFT).
- This script is best suited for educational/demo purposes.
- Works best when input length N is a power of two (e.g., 8, 16, 32, ...)

======================================================================
"""


from discrete_fourier_transforms import dft
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
    
def compare_time_complexity():
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
    
    #DFT [0(N^2)] time complexity
    start_dft=time.time()
    X_dft=dft(x)
    end_dft=time.time()
    print(f"DFT Execution Time :{end_dft-start_dft:.6f} s\n")
    
    #FFT [0(NlogN)] time complexity
    start_fft = time.time()
    X_fft= FFT(x)
    end_fft= time.time()
    print(f"FFT Execution Time: {end_fft - start_fft:.6f} s\n")
    return x,X_fft
    
    
def plot_fft(x,X):
    N=len(x)
    sampling_time=[0., 0.05, 0.1 , 0.15, 0.2 , 0.25, 0.3 , 0.35, 
       0.4 , 0.45, 0.5 ,
       0.55, 0.6 , 0.65, 0.7 , 0.75, 0.8 ,
       0.85, 0.9 , 0.95]
    
    sampling_rate=20
      
    #plot the FFT magnitude spectrum
    f_k=[ k*sampling_rate/len(X)  for k in range(len(X))]  
    X_k=[abs(val)for val in X]
    plt.stem(f_k[:N//2], X_k[:N//2], basefmt=" ", label="FFT Magnitude(s)")
    plt.legend()
    plt.grid()
    plt.title("FAST FOURIER TRANSFORMS")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude(|X[k]|)")    
    plt.show()
    print(f"frequency domain:{X}\n ")
    print(f"Magnitudes: {X_k}\n ")
    print(f"sampling time :{sampling_time}")
   
        
def main():
    x,X=compare_time_complexity()

    plot_fft(x,X)

if __name__=="__main__":
    main()

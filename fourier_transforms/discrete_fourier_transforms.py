"""
============================================================
Discrete Fourier Transform (DFT) 
------------------------------------------------------------


Description:
------------
This script computes the Discrete Fourier Transform (DFT) 
of a sampled signal using the DFT formula, and visualizes:

1. The original signal in the time domain
2. The magnitude spectrum in the frequency domain

Modules Used:
-------------
- cmath: For complex exponential calculations
- matplotlib.pyplot: For plotting graph

What it does:
-------------
- Uses a fixed 20-sample signal (x)
- Computes its DFT manually (not using NumPy FFT)
- Plots the original sampled signal over time
- Plots the DFT magnitude spectrum for frequencies

Notes:
------
- This is a basic educational implementation of DFT (O(N²) time)
- For performance with large signals, consider using FFT
- The sampling rate is assumed to be 20 Hz

============================================================
"""





import cmath
import matplotlib.pyplot as plt

def dft(x):
    N=len(x)
    X=[]
    sum=0
    for k in range(0,N):
       for n in range(0,N):
          sum +=x[n]*cmath.exp((-1j*2*cmath.pi*k*n)/N)
       X.append(sum)
       sum=0
    return X
    
def run_dft():
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
    X = dft(x)
    return x,X

def plot(x,X):
    N=len(x)
    
    sampling_time=[0., 0.05, 0.1 , 0.15, 0.2 , 0.25, 0.3 , 0.35, 
       0.4 , 0.45, 0.5 ,
       0.55, 0.6 , 0.65, 0.7 , 0.75, 0.8 ,
       0.85, 0.9 , 0.95]
    
    sampling_rate=20
    
    #plot the sampled wave
    plt.figure(figsize=(10, 4))
    plt.plot(sampling_time, x, 'o-', label='Sampled Signal')
    plt.title('Sampled Signal (Time Domain)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()

    #plot the DFT magnitude spectrum
    plt.figure(figsize=(10, 4))
    f_k=[ k*sampling_rate/len(X)  for k in range(len(X))]  
    X_k=[abs(val)for val in X]
    plt.stem(f_k[:N//2], X_k[:N//2], basefmt=" ", label="DFT Magnitude(s)")
    plt.legend()
    plt.grid()
    plt.title("DISCRETE FOURIER TRANSFORMS")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude(|X[k]|)")
    plt.show()
    
    print(f"frequency domain:{X}\n")
    print(f"Magnitudes: {X_k}\n")
    print(f"sampling time :{sampling_time}\n")

def main():
    x,X_dft = run_dft()
    plot(x,X_dft)
    
    
if __name__=="__main__":
        main()




      
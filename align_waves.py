"""
Given two sinusoids of two different frequencies,
Figure out how to change their frequencies at T such that at 2T, they would meet at the same value
"""
import numpy as np
import matplotlib.pyplot as plt

T = 4.06
f1 = 1.2
f2 = 2.1

times = np.arange(0, 2 * T + 0.01, 0.01)
g1_vals = []
g2_vals = []
for t in times:
    # figure out constants for g1(t)
    c_for_g1 = T * (f1 - f2) / f2
    # check for equal sign
    d_dt_g1 = f1 * np.sin(t)
    d_dt_g2 = f2 * np.sin(f2 * (t + c_for_g1))
    # If sign mismatch, move forward by 1
    if (d_dt_g1 >= 0 and d_dt_g2 < 0) or (d_dt_g1 < 0 and d_dt_g2 >= 0):
        c_for_g1 = T * (f1 - f2) / f2 - 1 / f2

    # firug out constants for g2(t)
    c_for_g2 = T * (f2 - f1) / f1
    # check for equal sign
    d_dt_g2 = f2 * np.sin(t)
    d_dt_g1 = f1 * np.sin(f1 * (t + c_for_g2))
    # If sign mismatch, move forward by 1
    if (d_dt_g1 >= 0 and d_dt_g2 < 0) or (d_dt_g1 < 0 and d_dt_g2 >= 0):
        c_for_g2 = T * (f2 - f1) / f1 - 1 / f1

    # dont flip until halfway
    if t < T:
        g1 = np.cos(2 * np.pi * f1 * t)
        g2 = np.cos(2 * np.pi * f2 * t)
    else:
        g1 = np.cos(2 * np.pi * f2 * (t + c_for_g1))
        g2 = np.cos(2 * np.pi * f1 * (t + c_for_g2))

    g1_vals += [g1]
    g2_vals += [g2]

print(f"g1: {g1_vals[-1]}, g2: {g2_vals[-1]}")
plt.title("freq over time")
plt.xlabel("time")
plt.plot(times, g1_vals, label=g1)
plt.plot(times, g2_vals, label=g2)
plt.legend()

plt.show()

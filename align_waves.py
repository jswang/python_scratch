"""
Given two sinusoids of two different frequencies,
Figure out how to change their frequencies at T such that at 2T, they would meet at the same value
"""
import numpy as np
import matplotlib.pyplot as plt

# length of time spend in one mode
T = 12.5 * 2
NUM_STRIP = 32
P1 = np.concatenate((np.arange(12.0, 13.01, 0.0625), np.arange(12.9375, 12.0, -0.0625)))
P2 = 25 - P1
F1 = 1 / P1
F2 = 1 / P2

# how long to run sim for
times = np.arange(0, 4 * T + 0.01, 0.01)


plt.title("freq over time")
plt.xlabel("time")
for i in range(NUM_STRIP):
    g1_vals = []
    f1 = F1[i]
    f2 = F2[i]
    for orig_t in times:
        t = orig_t % (T * 4)
        if t < 2 * T:
            # speeding up
            if t < T:
                g1 = 0.5 * (-np.cos(2 * np.pi * f1 * t) + 1)
            # slowing down
            else:
                # figure out constants for g1(t)
                c = T * (f1 - f2) / f2
                # check for equal sign
                d_dt_g1 = f1 * np.sin(f1 * t)
                d_dt_g2 = f2 * np.sin(f2 * (t + c))
                # If sign mismatch, move forward by 1
                if (d_dt_g1 >= 0 and d_dt_g2 < 0) or (d_dt_g1 < 0 and d_dt_g2 >= 0):
                    c -= 1 / f2
                g1 = 0.5 * (-np.cos(2 * np.pi * f2 * (t + c)) + 1)
        else:
            t -= 2 * T
            # slowing down
            if t < T:
                g1 = 0.5 * (-np.cos(2 * np.pi * f2 * t) + 1)
            # speeding up
            else:
                # figure out constants for g1(t)
                c = T * (f2 - f1) / f1
                # check for equal sign
                d_dt_g1 = f2 * np.sin(f2 * t)
                d_dt_g2 = f1 * np.sin(f1 * (t + c))
                # If sign mismatch, move forward by 1
                if (d_dt_g1 >= 0 and d_dt_g2 < 0) or (d_dt_g1 < 0 and d_dt_g2 >= 0):
                    c -= 1 / f1
                g1 = 0.5 * (-np.cos(2 * np.pi * f1 * (t + c)) + 1)

        g1_vals += [g1]
    plt.plot(times, g1_vals)


plt.legend()
plt.show()

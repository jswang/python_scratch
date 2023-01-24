"""
Given two sinusoids of two different frequencies,
Figure out how to change their frequencies at T such that at 2T, they would meet at the same value
"""
import numpy as np
import matplotlib.pyplot as plt

T = 12.5 * 4
NUM_STRIP = 32
P1 = np.concatenate((np.arange(12.0, 13.01, 0.0625), np.arange(12.9375, 12.0, -0.0625)))
P2 = 25 - P1
F1 = 1 / P1
F2 = 1 / P2

times = np.arange(0, 4 * T + 0.01, 0.01)


plt.title("freq over time")
plt.xlabel("time")
for i in range(NUM_STRIP):
    g1_vals = []
    f1 = F1[i]
    f2 = F2[i]
    for orig_t in times:
        t = orig_t % (T * 2)
        # dont flip until halfway
        if t < T:
            g1 = 0.5 * (-np.cos(2 * np.pi * f1 * t) + 1)
        else:
            # figure out constants for g1(t)
            c_for_g1 = T * (f1 - f2) / f2
            # check for equal sign
            d_dt_g1 = f1 * np.sin(t)
            d_dt_g2 = f2 * np.sin(f2 * (t + c_for_g1))
            # If sign mismatch, move forward by 1
            if (d_dt_g1 >= 0 and d_dt_g2 < 0) or (d_dt_g1 < 0 and d_dt_g2 >= 0):
                c_for_g1 -= 1 / f2
            g1 = 0.5 * (-np.cos(2 * np.pi * f2 * (t + c_for_g1)) + 1)

        g1_vals += [g1]
    plt.plot(times, g1_vals)


plt.legend()
plt.show()

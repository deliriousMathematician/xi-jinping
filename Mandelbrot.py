import numpy as np
import matplotlib.pyplot as plt

n_max = 50
threshold = 50

x = np.linspace(-2,1,10000)
y = np.linspace(-1.5,1.5,10000)

x, y = np.meshgrid(x, y)
c = x + y*1j

z = 0
for j in range(n_max):
    z = z ** 2 + c
z = np.sqrt(np.real(z)**2 + np.imag(z)**2)


xPlot = x[z < threshold]
yPlot = y[z < threshold]

plt.scatter(xPlot, yPlot, marker="o", s=0.005, color="black")
plt.show()





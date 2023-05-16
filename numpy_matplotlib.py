import numpy as np
import matplotlib.pyplot as plt

# Create an array of x values from 0 to 2*pi
x = np.linspace(0, 2*np.pi, 100)

# Create an array of y values representing the sine of x
y_sin = np.sin(x)

# Create an array of y values representing the cosine of x
y_cos = np.cos(x)

# Create a new figure
plt.figure()

# Plot the sine function
plt.plot(x, y_sin, label='sin(x)')

# Plot the cosine function
plt.plot(x, y_cos, label='cos(x)')

# Add a title
plt.title('Sine and Cosine Functions')

# Add an x-label
plt.xlabel('x')

# Add a y-label
plt.ylabel('y')

# Add a legend
plt.legend()

# Display the plot
plt.show()

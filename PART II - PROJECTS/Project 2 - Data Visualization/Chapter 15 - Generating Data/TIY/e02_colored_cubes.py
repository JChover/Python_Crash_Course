# 15-2 Colored Cubes - e02_colored_cubes.py
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10) # Use cmap to use a colormap, e.g., cmap=plt.cm.Blues

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range of each axes
ax.axis([0, 5100, 0, 135000000000])

plt.show()
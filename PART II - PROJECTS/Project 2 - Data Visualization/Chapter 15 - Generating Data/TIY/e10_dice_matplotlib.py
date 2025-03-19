# 15-10 Practicing with Both Libraries - e10_dice_matplotlib.py
import matplotlib.pyplot as plt

from e0x_die import Die

# Create two D8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results using matplotlib.
x_values = list(range(2, max_result+1))
fig, ax = plt.subplots()

ax.bar(x_values, frequencies, color='blue')

# Set labels and title
ax.set_title('Results of rolling two D8s 100,000 times', fontsize=14)
ax.set_xlabel('Result', fontsize=12)
ax.set_ylabel('Frequency of Result', fontsize=12)

# Set tick parameters for better readability
ax.tick_params(axis='both', labelsize=12)

# Show the plot
plt.show()

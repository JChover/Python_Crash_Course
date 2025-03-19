# Plotting Directions - rw_visual.py
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk- rw_visual.py
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

# Generating Multiple Random Walks - rw_visual.py
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk- rw_visual.py
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# Coloring the points - rw_visual.py
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk- rw_visual.py
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# Plotting the Starting and Ending Points - rw_visual.py
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk- rw_visual.py
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=15)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# Cleaning up the Axes - rw_visual.py
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk- rw_visual.py
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=15)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the Axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# Adding Plot Points - rw_visual.
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk(50_000) # Increase number of points to 50,000
    rw.fill_walk()

    # Plot the points in the walk- rw_visual.py
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the Axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# Altering the Size to Fill the Screen - rw_visual.py
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk(50_000) # Increase number of points to 50,000
    rw.fill_walk()

    # Plot the points in the walk- rw_visual.py
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the Axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
# 15-04 Modified Random Walk - e04_molecular_motion.py
import matplotlib.pyplot as plt

from e04_modified_random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk- rw_visual.py
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=2) # Using plot instead of scatter

    # Remove the Axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

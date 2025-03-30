# 15-05 Explore - e05_explore.py
import csv
from datetime import datetime

import matplotlib.pyplot as plt

sanfrancisco = 'data/san_francisco_2018_simple.csv'

with open(sanfrancisco) as f:
    reader = csv.reader(f)
    header = next(reader)

    # Get DATE, TAVG, TMAX and TMIN from this file
    dates, avgs, highs, lows = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
            avg = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            avgs.append(avg)
            dates.append(current_date)

# San Francisco - Plot the high and low temperatures and also average.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, avgs, c='orange', alpha=0.3)
ax.fill_between(dates, highs, avgs, facecolor='red', alpha=0.1)
ax.fill_between(dates, avgs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low and avg temperatures - 2018\nSan Francisco, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

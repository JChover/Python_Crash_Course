# 16-02 Sitka-Death Valley Comparison - e02_sitka_death_valley_comparison.py
import csv
from datetime import datetime

import matplotlib.pyplot as plt

deathv = 'data/death_valley_2018_simple.csv'
sitka = 'data/sitka_weather_2018_simple.csv'

with open(deathv) as f1:
    reader1 = csv.reader(f1)
    header1 = next(reader1)

    # Get DATE, TMAX and TMIN from this file
    dates1, highs1, lows1 = [], [], []
    for row1 in reader1:
        current_date1 = datetime.strptime(row1[2], '%Y-%m-%d')
        try:
            high1 = int(row1[4])
            low1 = int(row1[5])
        except ValueError:
            print(f"Missing data for {current_date1}")
        else:
            highs1.append(high1)
            lows1.append(low1)
            dates1.append(current_date1)

with open(sitka) as f2:
    reader2 = csv.reader(f2)
    header2 = next(reader2)

    # Get DATE, TMAX and TMIN from this file
    dates2, highs2, lows2 = [], [], []
    for row2 in reader2:
        current_date2 = datetime.strptime(row2[2], '%Y-%m-%d')
        try:
            high2 = int(row2[5])
            low2 = int(row2[6])
        except ValueError:
            print(f"Missing data for {current_date2}")
        else:
            highs2.append(high2)
            lows2.append(low2)
            dates2.append(current_date2)

# Death Valley - Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig1, ax1 = plt.subplots()
ax1.set_ylim(20, 150)
ax1.plot(dates1, highs1, c='red', alpha=0.5)
ax1.plot(dates1, lows1, c='blue', alpha=0.5)
ax1.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig1.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Sitka - Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig2, ax2 = plt.subplots()
ax2.set_ylim(20, 150)
ax2.plot(dates2, highs2, c='red', alpha=0.5)
ax2.plot(dates2, lows2, c='blue', alpha=0.5)
ax2.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nSitka, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig2.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

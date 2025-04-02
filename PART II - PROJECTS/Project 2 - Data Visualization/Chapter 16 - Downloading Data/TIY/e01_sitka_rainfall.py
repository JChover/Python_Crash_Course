# 16-01 Sitka Rainfall - e01_sitka_rainfall.py
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    # Get DATE and PRCP from this file
    dates, precipitations = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        prec = float(row[3])
        precipitations.append(prec)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c='purple')

# Format plot.
plt.title("Daily Precipitations, Sitka - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

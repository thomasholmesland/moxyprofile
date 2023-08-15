import numpy as np
import matplotlib.pyplot as plt

#calculate sloperate from a list
seconds = 180
slope_seconds_start = 0
seconds_minute_in = seconds - 60
slope_start = [74, 60, 60, 65, 63]
slope_minute = [55, 52, 56, 51, 44]
slope_end = [57, 55, 55, 48, 29]
average_heartrate = [128, 128, 144, 156, 166]
average_power = [245, 306, 349, 385, 429]
lactate = [2, 2.1, 2.7, 4.5, 7.9]
duration = [seconds, seconds*2, seconds*3, seconds*4, seconds*5]

def slope_utregning(slope_seconds_start, slope_start, seconds, slope_end):
    if (slope_end - slope_start != 0):
        return (float(slope_end - slope_start) / (seconds - slope_seconds_start))
    return None

slope_calculated_beginning = []

for i in range(len(slope_start)):
    slope = slope_utregning(slope_seconds_start, slope_start[i], seconds, slope_end[i])
    slope_calculated_beginning.append(slope)

print(f"Sloperate for the whole interval: {slope_calculated_beginning}")

def slope_utregning_minute(slope_seconds_start, slope_start, seconds, slope_end):
    if (slope_end - slope_start != 0):
        return (float(slope_end - slope_start) / (seconds - slope_seconds_start))
    return None

slope_calculated_minute = []

for i in range(len(slope_minute)):
    slope = slope_utregning_minute(slope_seconds_start, slope_minute[i], seconds_minute_in, slope_end[i])
    slope_calculated_minute.append(slope)

print(f"Sloperate for one minute into the interval: {slope_calculated_minute}")

correlation_coefficient_beginning = np.corrcoef(lactate, slope_calculated_beginning)[0, 1]
correlation_coefficient_minute = np.corrcoef(lactate, slope_calculated_minute)[0, 1]
correlation_coefficient_heartrate = np.corrcoef(lactate, average_heartrate)[0, 1]
correlation_coefficient_power = np.corrcoef(lactate, average_power)[0, 1]

fig, ax = plt.subplots()
plt.rcParams["figure.figsize"] = (10, 10)
plt.subplot(3, 2, 1)
plt.scatter(average_power, lactate, c="red", label="Lactate")
plt.scatter(average_power, slope_calculated_minute, c="blue", label="Slope from one minute in")
plt.axis([200, 450, -2, 10])
plt.xlabel("Power")
plt.ylabel("Sloperate")
plt.text(0.95, 0.95, f"r From one minute in = {correlation_coefficient_minute:.4f}",
         transform=plt.gca().transAxes,
         verticalalignment='top', horizontalalignment='right')
plt.legend(loc="upper left")

plt.subplot(3, 2, 2)
plt.scatter(average_power, lactate, c="red", label="Lactate")
plt.scatter(average_power, slope_calculated_beginning, c="blue", label="Slope from beginning")
plt.axis([200, 450, -2, 10])
plt.xlabel("Power")
plt.ylabel("Sloperate")
plt.text(0.95, 0.95, f"r From the beginning = {correlation_coefficient_beginning:.4f}",
         transform=plt.gca().transAxes,
         verticalalignment='top', horizontalalignment='right')
plt.legend(loc="upper left")

plt.subplot(3, 2, 3)
plt.scatter(average_power, average_heartrate, c="red")
plt.text(0.95, 0.95, f"r = {correlation_coefficient_heartrate:.4f}",
         transform=plt.gca().transAxes,
         verticalalignment='top', horizontalalignment='right')
plt.axis([200, 450, 120, 180])
plt.xlabel("Power")
plt.ylabel("Average heartrate")

plt.subplot(3, 2, 4)
plt.scatter(average_power, lactate, c="red")
plt.text(0.95, 0.95, f"r = {correlation_coefficient_power:.4f}",
         transform=plt.gca().transAxes,
         verticalalignment='top', horizontalalignment='right')
plt.axis([200, 450, 0, 10])
plt.xlabel("Average power")
plt.ylabel("Lactate")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
data = pd.read_csv("epa-sea-level.csv")

# Create scatter plot of data
plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"])

# Get slope and y-intercept of line of best fit using all data
slope, intercept, _, _, _ = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
# Plot line of best fit going through year 2050
plt.plot(data["Year"], data["Year"]*slope + intercept)

# Get slope and y-intercept of line of best fit using data from 2000 onwards
slope, intercept, _, _, _ = linregress(data[data["Year"] >= 2000]["Year"], data[data["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
# Plot line of best fit going through year 2050
plt.plot(data["Year"], data["Year"]*slope + intercept)

plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.show()

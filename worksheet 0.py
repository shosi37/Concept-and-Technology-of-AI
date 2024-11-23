#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task 1: Classify Temperatures

temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
                16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3,
                13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7,
                7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3,
                16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5]

# Initialize empty lists
cold = []
mild = []
comfortable = []

# Classify temperatures
for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp <= 20:
        comfortable.append(temp)

# Print classifications
print("Cold temperatures:", cold)
print("Mild temperatures:", mild)
print("Comfortable temperatures:", comfortable)


# Task 2: Analyze Data

# Count occurrences in each category
print("Number of cold days:", len(cold))
print("Number of mild days:", len(mild))
print("Number of comfortable days:", len(comfortable))



# Task 3: Convert Temperatures to Fahrenheit

# Convert Celsius to Fahrenheit
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]

# Print converted values
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)



# Task 4: Analyze Temperature Patterns by Time of Day

# Group by time of day
night = temperatures[::3]  # Every 3rd starting from index 0
evening = temperatures[1::3]  # Every 3rd starting from index 1
day = temperatures[2::3]  # Every 3rd starting from index 2

# Calculate average day-time temperature
average_day_temp = sum(day) / len(day)

# Print results
print("Night temperatures:", night)
print("Evening temperatures:", evening)
print("Day temperatures:", day)
print("Average day-time temperature:", average_day_temp)


# Optional: Plot "Day vs. Temperature"

import matplotlib.pyplot as plt

# Plot day vs temperature
plt.plot(range(1, len(day) + 1), day, marker='o', label='Day Temperatures')
plt.title("Day vs Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()



# In[ ]:





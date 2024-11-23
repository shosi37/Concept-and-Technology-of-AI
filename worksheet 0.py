#!/usr/bin/env python
# coding: utf-8

# In[25]:


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



# In[1]:


def sum_nested_list(nested_list):
    """
    Recursively sums all numbers in a nested list.

    Args:
    nested_list (list): A list that may contain numbers or other lists of numbers.

    Returns:
    int: The total sum of all numbers in the nested list.
    """
    total = 0
    for item in nested_list:
        if isinstance(item, list):  # If the item is a list, call the function recursively
            total += sum_nested_list(item)
        else:  # If the item is a number, add it to the total
            total += item
    return total

# Test the function
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
result = sum_nested_list(nested_list)
print(f"Total sum of {nested_list} is: {result}")


# In[2]:


def generate_permutations(s):
    if len(s) == 1:
        return [s]  # Base case: a single character has only one permutation

    # To store all unique permutations
    permutations = set()

    for i, char in enumerate(s):
        # Remove the character at index i and get the rest of the string
        remaining = s[:i] + s[i+1:]
        # Generate permutations of the remaining string
        for perm in generate_permutations(remaining):
            # Add the current character to the front of each permutation
            permutations.add(char + perm)

    return list(permutations)  # Convert the set to a list

# Test the function
print("Permutations of 'abc':", generate_permutations("abc"))
print("Permutations of 'aab':", generate_permutations("aab"))


# In[3]:


def calculate_directory_size(directory):
    total_size = 0

    for key, value in directory.items():
        if isinstance(value, dict):  # If the value is a dictionary, it's a subdirectory
            total_size += calculate_directory_size(value)
        else:  # Otherwise, it's a file size
            total_size += value

    return total_size

# Sample directory structure
directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}

# Test the function
total_size = calculate_directory_size(directory_structure)
print(f"Total size of the directory: {total_size} KB")


# In[4]:


def min_coins(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount using dynamic programming.

    Parameters:
    coins (list of int): A list of coin denominations available for making change.
    amount (int): The target amount for which we need to find the minimum number of coins.

    Returns:
    int: The minimum number of coins required to make the given amount.
         If it is not possible to make the amount with the given coins, returns -1.
    """
    # Initialize a DP array with infinity for all amounts greater than 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Build up the DP array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result
    return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
print("Minimum coins for amount 11 with coins [1, 2, 5]:", min_coins([1, 2, 5], 11))  # Expected output: 3
print("Minimum coins for amount 3 with coins [2]:", min_coins([2], 3))  # Expected output: -1


# In[5]:


def knapsack(weights, values, capacity):
    n = len(weights)
    
    # Create a DP table with (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value will be in dp[n][capacity]
    return dp[n][capacity]

# Test with the provided example
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
result = knapsack(weights, values, capacity)
print(f"The maximum value that can be carried is: {result}")


# In[ ]:





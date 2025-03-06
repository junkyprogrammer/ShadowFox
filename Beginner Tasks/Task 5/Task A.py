#Adding libraries

import random

# Initialize counters

dice_r1 = 0
dice_r6 = 0
dice_r6_twice = 0

# Previous roll variable to check for two 6s in a row
previous_roll = None

# Simulate rolling a six-sided die 20 times
for _ in range(20):
  roll = random.randint(1, 6)
  print(f"Rolled: {roll}")
  
  # Count occurrences of 1 and 6
  if roll == 1:
    dice_r1 += 1
  elif roll == 6:
    dice_r6 += 1
    # Check for two 6s in a row
    if previous_roll == 6:
      dice_r6_twice += 1
  
  # Update previous roll
  previous_roll = roll

# Print statistics
print(f"Number of times rolled a 1: {dice_r1}")
print(f"Number of times rolled a 6: {dice_r6}")
print(f"Number of times rolled two 6s in a row: {dice_r6_twice}")


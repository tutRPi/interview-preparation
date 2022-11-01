from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  last_eaten = []
  counter = 0
  for dish in D:
    if dish not in last_eaten:
      counter += 1
      last_eaten.append(dish)
      if len(last_eaten) > K:
        last_eaten.pop(0)
  return counter

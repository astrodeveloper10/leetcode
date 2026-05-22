# Two Sum I

## Brute force Approach

For the brute-force approach, I'll use two nested loops:

- The outer loop fixes one element
- The inner loop checks all elements to the right of it
- When we find two numbers that sum to the target, we return their indices
- If no match is found, we return an empty list

This way, we check every possible pair without using the same index twice.

Time: O(n²) - nested loops
Space: O(1) - no extra data structures

## Optimal Approach

- Use a hashmap to store numbers and their indices as we traverse
  - Key = number value
  - Value = index position
  
- For each number in the array:
  - Calculate the complement: `complement = target - current_number`
  - Check if the complement exists in the hashmap
  - If yes, return both indices [hashmap[complement], current_index]
  - If no, add the current number and index to the hashmap

- Time Complexity: O(n) - single pass through the array
- Space Complexity: O(n) - hashmap storage

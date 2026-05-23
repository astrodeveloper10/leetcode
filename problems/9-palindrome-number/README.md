# Palindrome Number

A number is a palindrome if it reads the same forwards and backwards.

## Key Insights

- Negative numbers cannot be palindromes (have "-" prefix)
- Numbers ending in 0 cannot be palindromes (except 0 itself)
- We can reverse half the number instead of converting to string

## Algorithm

1. **Check edge cases:**
   - Return false if negative or ends with 0 (but not 0 itself)

2. **Reverse the second half:**
   - Extract the last digit and build the reversed number
   - Continue until we've processed half the digits (x ≤ reverse_x)

3. **Compare halves:**
   - For even-length: x == reverse_x
   - For odd-length: x == reverse_x // 10 (ignore middle digit)

## Complexity

- **Time:** O(log n) - number of digits
- **Space:** O(1) - constant extra space

## Edge Cases

- `-121`: Not a palindrome
- `0`: Is a palindrome
- `10`: Not a palindrome (ends in 0)
- `9`: Is a palindrome (single digit)

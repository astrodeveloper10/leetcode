# Remove Duplicates from Sorted Array - Interview Explanation

## Problem Overview

Remove duplicates from a sorted array in-place and return the count of unique elements.

---

## Solution Approach (30 seconds)

This is a **two-pointer technique**. Since the array is sorted, duplicates are always adjacent. We use:

- **`slow` pointer**: marks where unique elements should go
- **`fast` pointer**: scans through the array looking for new unique values

---

## How It Works (Detailed Explanation)

### The Core Logic

1. `slow` starts at index 0 (first element is always unique)
2. `fast` scans from index 1 onwards
3. When `fast` finds a value **different** from `nums[slow]`:
   - Increment `slow` to the next position
   - Place that new unique value at `nums[slow]`
4. Return `slow + 1` (the count of unique elements)

### Why It Works

- In a sorted array, duplicates are adjacent
- By moving `slow` only when we find something new, we naturally keep all unique values at the front
- Elements after position `slow` don't matter—they're just overwritten

## Complexity Analysis

| Metric | Value | Reasoning |
| -------- | ------- | ----------- |
| **Time Complexity** | O(n) | Single pass through array with fast pointer |
| **Space Complexity** | O(1) | Modify in-place, no extra data structures |

---

## Key Talking Points

✅ **Two-pointer pattern**: Classic technique for array problems  
✅ **In-place modification**: No extra space needed  
✅ **Sorted array assumption**: Duplicates are adjacent  
✅ **Index vs. count**: Return `slow + 1` because slow is a 0-indexed position  

---

## Common Interview Follow-ups

### Q1: Why not use a set?

**A:** "A set would be O(n) space. This two-pointer approach solves it in-place with O(1) space—better for memory-constrained scenarios like embedded systems or large datasets."

### Q2: What if the array isn't sorted?

**A:** "Then we'd need a different approach:

- Use a HashSet to track seen values: O(n) time, O(n) space
- Or sort first, then use this approach: O(n log n) time, O(1) space
- Or use a HashMap to count occurrences"

### Q4: Why do we need `slow + 1`?

**A:** "`slow` is an index (0-based), so it points to the last unique element. Adding 1 gives us the count. For example, if slow=2, we have elements at indices 0, 1, 2 = 3 elements total."

---

## Variations of This Problem

| Variation | Modification |
| ----------- | -------------- |
| **Remove duplicates II** (allow max 2) | Check `slow < 2 or nums[fast] != nums[slow-2]` |
| **Remove specific value** | Check `if nums[fast] != target` |
| **Remove at most k duplicates** | Track count with additional variable |

---

## Tips for Interview Success

1. **Explain before coding**: Walk through your approach first
2. **Use concrete examples**: Trace through with actual numbers
3. **Discuss trade-offs**: Time vs. space, simplicity vs. optimization
4. **Write clean code**: Use meaningful variable names, add comments
5. **Test edge cases**: Empty array, single element, all duplicates, no duplicates

---

## Edge Cases to Consider

```python
# Test these:
removeDuplicates([])                    # []
removeDuplicates([1])                   # [1]
removeDuplicates([1,1])                 # [1]
removeDuplicates([1,2,3])               # [1,2,3]
removeDuplicates([1,1,1,1,1])           # [1]
removeDuplicates([1,1,2,2,2,3,3,4])     # [1,2,3,4]
```

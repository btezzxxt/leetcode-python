# 41 first missing positive

```python
class Solution(object): def firstMissingPositive(self, nums): """ :type nums: List[int] :rtype: int """ def checkAndReplace(cur_index, nums): cur_value = nums[cur_index] target_index = cur_value-1 # value large positive, set to -1 as if swapped if target_index >= len(nums): nums[cur_index] = -1 return False
 # already at right location if nums[target_index] == cur_value: # if target_index != cur_index and the pos is set, set cur to -1 if target_index != cur_index: nums[cur_index] = -1 return False if nums[target_index] <= 0: temp = nums[target_index] nums[target_index] = nums[cur_index] nums[cur_index] = temp return False else: temp = nums[target_index] nums[target_index] = nums[cur_index] nums[cur_index] = temp return True return False if (len(nums) == 0): return 1
 for i in range(len(nums)): cur_value = nums[i] target_index = cur_value-1
 if target_index == i: # right position continue if cur_value <= 0: continue else: # positive number # pre-check target location nums[cur_value]
 while checkAndReplace(i, nums): continue continue for i in range(len(nums)): if nums[i] <= 0: return i + 1 return len(nums) + 1



print(Solution().firstMissingPositive([2,1]))


```


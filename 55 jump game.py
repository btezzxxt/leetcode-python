class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_pos = 0
        cur_val = nums[0]
        reachable = cur_pos+cur_val
        destination = len(nums) - 1
        while reachable < destination:
            if cur_pos < reachable:
                cur_pos += 1
                cur_val = nums[cur_pos]
                cur_reachable = cur_pos + cur_val
                reachable = max(cur_reachable, reachable)
            else:
                return False 

        return True 

print(Solution().canJump([2,1,0,0,4]))
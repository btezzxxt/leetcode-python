class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # wierd case [0]         
        if len(nums) == 1:
            return 0
        
        step = 1
        cur_pos = 0
        cur_val = nums[0]
        cur_reachable = cur_pos+cur_val
        next_reachable = cur_reachable
        
        jump_at = {cur_pos: cur_val}
        path = [jump_at]

        destination = len(nums) - 1
        while cur_reachable < destination:
            if cur_pos < cur_reachable:
                cur_pos += 1
                cur_val = nums[cur_pos]
                cur_pos_reachable = cur_pos + cur_val
                if cur_pos_reachable > next_reachable:
                    next_reachable = cur_pos_reachable
                    jump_at = {cur_pos: cur_val}
            else:
                if next_reachable == cur_reachable:
                    print(path)
                    return 0
                else:
                    cur_reachable = next_reachable
                    step += 1
                    path.append(jump_at)

        print(path)
        return step 

print(Solution().jump([2,3,1,1,4,1,3,4,2,1,3,4,5,1,1,2,1,1,2,1,1,3]))

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                ret.append(nums.index(target - nums[i]))
                ret.append(i)
                return ret
            else:
                hashset.add(target-nums[i])
            
print (__name__)
   
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))

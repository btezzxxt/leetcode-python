# class Solution:
#     def smallestDistancePair(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         #going to find a number m, count all distence <= m, let total count > k
#         nums.sort()
#         n = len(nums)
#         l = 0 # this can't be nums[1] - nums[0] since can't ensure that its the min
#         r = nums[-1] - nums[0] #can ensure this is the max
#         while l <= r: 
#             m = l + (r-l)//2
#             i=0 
#             dp={}
#             j=1
#             count=0
#             while i<n:                                          #i, j will always increase, so time complex is O(2n)
#                 while j<n and nums[j] - nums[i] <=m:
#                     j+=1
#                 count+=j-i-1
#                 dp[i] = count                                   #the dp here shows the storage of counts <=m when i as minuend, O(n) space; -> count O(1) space
#                 i+=1
#             if count>=k:
#                 r=m-1
#             else:
#                 l=m+1
#         return l                                                #return l 
    
# print(Solution().smallestDistancePair([38,33,57,65,13,2,86,75,4,56],26))

class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #going to find a number m, count all distence <= m, let total count > k
        nums.sort()
        start = 0 # this can't be nums[1] - nums[0] since can't ensure that its the min
        end = nums[-1] - nums[0] #can ensure this is the max
        return bs_find_target(start, end, k, nums)    

def count_all_pair_dis_lt_eq_m(m, nums):
    n = len(nums)
    count = 0
    i = 0
    j = 1
    while i<n:                                          #i, j will always increase, so time complex is O(2n)
        while j<n and nums[j] - nums[i] <=m:
            j+=1
        count+=j-i-1
        i+=1
    return count

def bs_find_target(start, end, k, nums):
    l = start
    r = end
    while l<=r:
        m=l+(r-l)//2
        if count_all_pair_dis_lt_eq_m(m, nums) >= k:
            r = m - 1
        else:
            l = m + 1
    return l

print(Solution().smallestDistancePair([38,33,57,65,13,2,86,75,4,56],26))

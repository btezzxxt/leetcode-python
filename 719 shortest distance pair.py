class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #going to find a m, count all distence <= m, let total count > k
        nums.sort()
        n = len(nums)
        l = 0 # this can't be nums[1] - nums[0] since can't ensure that its the min
        r = nums[-1] - nums[0] #can ensure this is the max
        while l <= r: 
            m = l + (r-l)//2
            i=0 
            dp={}
            j=1
            count=0
            while i<n:
                while j<n and nums[j] - nums[i] <=m:
                    j+=1
                count+=j-i-1
                dp[i] = count
                i+=1
            if count>=k:
                r=m-1
            else:
                l=m+1
        return l
    
print(Solution().smallestDistancePair([9,10,7,10,6,1,5,4,9,8],18))
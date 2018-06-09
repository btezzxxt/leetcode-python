# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
     return '[' + str(self.start) + ',' + str(self.end) + ']'
    def __repr__(self):
     return '[' + str(self.start) + ',' + str(self.end) + ']'     

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def bs_i_max_eq_key(nums, key):
            l = 0 
            r = len(nums)-1
            while l < r:
                m = l + (r-l+1) // 2
                if nums[m].start > key:
                    r = m - 1
                else:
                    l = m
            if nums[l].start == key:
                return l
            return -1

        def bs_i_max_lt_key(nums, key):
            l = 0 
            r = len(nums)-1
            while l < r:
                m = l + (r-l+1) // 2
                if nums[m].start >= key:
                    r = m - 1
                else:
                    l = m
            if nums[l].start < key:
                return l
            return -1    

        def bs_i_min_eq_key(nums, key):
            l = 0
            r = len(nums) -1
            while l < r:
                m = l + (r-l) // 2
                if nums[m].end < key:
                    l = m + 1
                else:
                    r = m
            if nums[r].end == key:
                return r
            return -1

        def bs_i_min_gt_key(nums, key):
            l = 0
            r = len(nums) -1
            while l < r:
                m = l + (r-l) // 2
                if nums[m].end <= key:
                    l = m + 1
                else:
                    r = m
            if nums[r].end > key:
                return r
            return -1

        left = bs_i_max_eq_key(intervals, newInterval.start)
        if left == -1:
            left = bs_i_max_lt_key(intervals, newInterval.start)
        
        right = bs_i_min_eq_key(intervals, newInterval.end)
        if right == -1:
            right = bs_i_min_gt_key(intervals, newInterval.end)
        
        if left == -1 or right == -1:
            return intervals
        else:
            lInterval = intervals[left]
            rInterval = intervals[right]
            newStart = 0
            newEnd = 0
            leftPart = intervals[:left]
            rightPart = intervals[right+1:]
            if lInterval.end > newInterval.start:
                newStart = lInterval.start
            else:
                leftPart.append(lInterval)
                newStart = newInterval.start
            
            if rInterval.start < newInterval.end:
                newEnd = rInterval.end
                leftPart.append(Interval(newStart, newEnd))
            else:
                newEnd = newInterval.end
                leftPart.append(Interval(newStart, newEnd))
                leftPart.append(intervals[right])
            return leftPart + rightPart

print(Solution().insert([Interval(1,3),Interval(6,9)], Interval(2,5)))

print(Interval(1,3))




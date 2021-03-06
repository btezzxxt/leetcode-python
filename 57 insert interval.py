# O(logn) time complexity, beats 99.68% :p

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

        if len(intervals) == 0:
            return [newInterval]
        
        left = bs_i_max_eq_key(intervals, newInterval.start)
        if left == -1:
            left = bs_i_max_lt_key(intervals, newInterval.start)
        
        right = bs_i_min_eq_key(intervals, newInterval.end)
        if right == -1:
            right = bs_i_min_gt_key(intervals, newInterval.end)
        

        leftPart = []
        if left == -1:
            newStart = newInterval.start
        else:
            lInterval = intervals[left]
            leftPart = intervals[:left]
            if lInterval.end >= newInterval.start:
                newStart = lInterval.start
            else:
                leftPart.append(lInterval)
                newStart = newInterval.start 
        if right == -1:
            newEnd = newInterval.end
            leftPart.append(Interval(newStart, newEnd))
        else:
            rInterval = intervals[right]
            rightPart = intervals[right+1:]
            if rInterval.start <= newInterval.end:
                newEnd = rInterval.end
                leftPart.append(Interval(newStart, newEnd))
            else:
                newEnd = newInterval.end
                leftPart.append(Interval(newStart, newEnd))
                leftPart.append(intervals[right])
            leftPart += rightPart
        return leftPart

print(Solution().insert([Interval(1,3),Interval(6,9)], Interval(2,5)))



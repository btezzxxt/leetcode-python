class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1] #set a start for calculating the first bar
        heights.append(0) #make sure all items > 0 can be popped out of stack
        largest = 0 
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                cur_index = stack.pop()
                height = heights[cur_index]
                width = i - 1 - stack[-1]
                largest = max(largest, height*width)
            stack.append(i)
        return largest

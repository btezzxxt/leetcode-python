class Solution(object):
     def findMedianSortedArrays(self, nums1, nums2):
        def getKthNum(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            if k == 0:
                return min(nums1[0], nums2[0])
            len1 = len(nums1)
            len2 = len(nums2)

            mid_num1_i = len1//2
            mid_num2_i = len2//2
            mid_num1_value = nums1[mid_num1_i] 
            mid_num2_value = nums2[mid_num2_i]

            if (mid_num1_value<mid_num2_value):
                if (k>mid_num1_i+mid_num2_i):
                    return getKthNum(nums1[mid_num1_i+1:], nums2, k-mid_num1_i-1)
                else:
                    return getKthNum(nums1, nums2[:mid_num2_i], k)
            else:
                if (k>mid_num2_i+mid_num1_i):
                    return getKthNum(nums1, nums2[mid_num2_i+1:], k-mid_num2_i-1)
                else:
                    return getKthNum(nums1[:mid_num1_i], nums2, k)

        length = len(nums1) + len(nums2)
        if (length %2==1):
            return getKthNum(nums1,nums2,length//2)/1.0
        else:
            return (getKthNum(nums1,nums2,length//2) + getKthNum(nums1,nums2,length//2-1))/2.0

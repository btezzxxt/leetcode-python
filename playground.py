#binary search practice again
def bs_max_i_lt_key(nums, key):
    l = 0
    r = len(nums) - 1
    while l<r:
        m = l + (r - l +1)//2 # use l to identify need plus one
        if (nums[m]>=key):
            r=m-1
        else:
            l=m # use l, set l=m in else
    if nums[l] < key:
        return l
    return -1

print(bs_max_i_lt_key([1,2,2,3,3,3,4,4,5,5,7], 1))

def bs_max_i_eq_key(nums, key):
    l =0
    r =len(nums)-1
    while l<r:
        m = l+(r-l+1)//2
        if(nums[m]>key):
            r=m-1
        else:
            l=m
    if nums[l]==key:
        return l
    return -1

print(bs_max_i_eq_key([1,2,2,3,3,3,4,4,5,5,7], 3))

def bs_min_i_gt_key(nums, key):
    l=0
    r=len(nums)-1
    while l<r:
        m=l+(r-l)//2
        if nums[m]<=key:
            l=m+1
        else:
            r=m

    if nums[r] > key:
        return r
    return -1

print(bs_min_i_gt_key([1,1,2,2,2,3,3,4,5,6,7,7],2))

def bs_min_i_eq_key(nums, key):
    l=0
    r=len(nums)-1
    while l<r:
        m=l+(r-l)//2
        if nums[m]<key:
            l=m+1
        else:
            r=m
    if(nums[r]==key):
        return r
    return -1

print(bs_min_i_eq_key([1,1,2,2,2,3,3,4,5,6,7,7],2))

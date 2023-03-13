
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


def binarySearch(alist, item):
    
    def binarySearch(list, item):
        first = 0
        last = len(list)-1
        found = False
        while first<=last and not found:
            pos = 0
            midpoint = (first + last)//2
            if list[midpoint] == item:
                pos = midpoint
                found = True
                return (pos)
            else:
                if item < list[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return -1

    list1 = alist[:alist.index(min(alist))]
    list2 = alist[alist.index(min(alist)):]
    
    if binarySearch(list1, item) != -1:
        return binarySearch(list1, item)
    
    elif binarySearch(list2, item) != -1:
        return len(list1) + binarySearch(list2, item)
    
    else:
        return -1



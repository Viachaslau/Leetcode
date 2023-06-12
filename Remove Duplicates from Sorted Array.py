
def removeDuplicates():
    nums = [1,1,2]
    k = len(nums)
    val_prev = nums[0]
    for val in nums[1:]:
        if  val_prev == val:
            nums.remove(val)
            nums.append('_')
            k -= 1
        val_prev = val  
    return k, nums
    
print(removeDuplicates())


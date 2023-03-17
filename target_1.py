import math
nums = [3,0,5,6,7,8,9,1,5]
# target 6
i=0  
for nums[i] in nums:
    if nums[i]+nums[i+1]==6:
        print(list[i,i+1])
        i+=1
        break
    else:
        i+=1
       
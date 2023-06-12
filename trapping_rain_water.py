height = [1,0,9]
total_water = 0
for p in range(len(height)):
    left_p = p
    right_p = p
    max_left = 0
    max_right = 0
    while left_p >= 0: # Determining the left-max value for the current element at the index p is pointing
        max_left = max(max_left,height[left_p])
        left_p -= 1
    while right_p < len(height): #Determining the right-max value for the current element at the index p is pointing
        max_right = max(max_right,height[right_p])
        right_p += 1
    trap_water = min(max_left,max_right) - height[p]
    #Calculating the water can be trapped in the current element at the index P pointing
    if trap_water > 0:
        total_water += trap_water
print(total_water)
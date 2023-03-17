import numpy as np

list1 = [9,0,6,5,4,3,4,5,6,7,8,9,9,8,6,5,4,3,2]
if list1 == []:
    result_list = list1
else:
    if len(list1) % 2 == 0:
        num_list = len(list1)//2
    else:
        num_list = (len(list1)//2) + 1

    sub_lists = np.array_split(list1, num_list)
    count=1
    result_list = []
    for i in sub_lists:
        list2 = list(i)
        list2.reverse()
        result_list += list2
        count+=1
print(result_list)
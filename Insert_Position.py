# Iterative Binary Search Function
# It returns the index of x in the given list if present,
# else returns -1
def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    mid = 0
    
    a=lst.copy()
    if len(lst)<=2:
        print(a)
        a.append(x)
        a.sort()
        return(a.index(x))

    else:

        while low <= high and len(lst)>2:

            mid = (high + low) // 2

            # If x is greater, ignore the left half
            if lst[mid] < x:
                low = mid + 1

                # If x is smaller, ignore the right half
            elif lst[mid] > x:
                high = mid - 1

                # means x is present in mid
            else:
                a=f'Element is present at index: {mid}'
                return a

            # If we reach here, then the element was not present
        
        low = 0
        high = len(lst) - 1
        if x>=lst[high] or lst[low]<x<lst[low+1]:
            b = f'Element is not present in list, but if we want to put it in order it will be indexes: {mid+1}.'
        else:
            b = f'Element is not present in list, but if we want to put it in order it will be indexes: {mid}.'
    return b


# Test list
lst = [1,3]
x = 1
print(binary_search(lst, x))

 
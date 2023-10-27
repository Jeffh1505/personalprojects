def get_number(li, s):
    for i in li:
        if s in li:
            return True
        else:
            return False
        

c = get_number([1,5,9,15,25,47, 360], 3)
print(c)


def get_number_binary(arr, low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return True
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return get_number_binary(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return get_number_binary(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return False
    
a = get_number_binary([1,2,3,4,5,6,7], 1, 7, 9)
print(a)
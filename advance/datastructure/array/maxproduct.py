import array as arr
def max_Product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        print("No pairs exists") 
        return      
    # Initialize max product pair 
    x = arr[0]; y = arr[1] 

    # Traverse through every possible pair     
    for i in range(0, arr_len): 

        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 

    return x,y    

nums = arr.array("i",[1, 2, 3, 4, 7, 0, 8, 4]) 
print("Original array:", nums)
print("Maximum product pair is:", max_Product(nums))

nums = arr.array("i",[0, -1, -2, -4, 5, 0, -6])
print("\nOriginal array:", nums)
print("Maximum product pair is:", max_Product(nums))

def bubblesort(unsorted_list):
    for index in range(len(unsorted_list)-1,0,-1):
        for i in range(index):
            if unsorted_list[i] > unsorted_list[i+1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = temp
    return unsorted_list

unsorted_list = [4,7,2,4,9,10,11,16,45]
print("without sorted",unsorted_list)
print("sorted",bubblesort(unsorted_list))
    
    
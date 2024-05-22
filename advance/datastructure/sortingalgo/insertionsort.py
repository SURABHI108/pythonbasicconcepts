def insertionSort(unsorted_list):
    for i in range(0,len(unsorted_list)):
        key = unsorted_list[i]

        j =i-1
        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1
            unsorted_list[j+1] = key
    return unsorted_list;

unsorted_list = [43,54,67,89,3,2]
print("without sorting",unsorted_list)
print("sorting",insertionSort(unsorted_list))  
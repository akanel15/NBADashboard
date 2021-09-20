"""
(Stable) Counting sort
This function takes an array as an input and sorts its elements into order
It does this using a count array and a position array and outputs a stable sorted array
"""

def counting_sort(sorting_arr, init_arr):
    m = max(sorting_arr) # find the max element to form count and position arrays
    count = [0] * (m+1)
    pos = [0] * (m+1)

    for item in sorting_arr:
        count[item] += 1
        # determining the number of each element in the array

    for j in range(1,len(count)):
        pos[j] = pos[j-1] + count[j-1]
        # using count array to determine the position each item will go


    output_arr = [0] * len(sorting_arr)

    for i in range(len(sorting_arr)):
        output_arr[pos[sorting_arr[i]]] = init_arr[i] # finding the position that element goes and storing
        pos[sorting_arr[i]] += 1 # incrementing the position to know where the next one will go
    return output_arr
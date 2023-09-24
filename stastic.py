import numpy as np
def root():
    print("Welcome Static")
    main_input = input()
    str_arr = list(main_input)
    int_arr = int_list = [int(x) for x in str_arr]
    print("your arr: ",int_arr)
    sorted_arr = sorted(int_arr)
    print("softed arr: ",sorted_arr)
    print('arr_len: ',len(sorted_arr))
    find_mean(sorted_arr)
    find_meian(sorted_arr)
    find_mode(sorted_arr)
    find_Q1_Q2_Q3(sorted_arr)
    find_outliner(sorted_arr)

def find_outliner(arr):
    data = np.array(arr)

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    lower_outliers = data[data < lower_bound]
    upper_outliers = data[data > upper_bound]
    print("Lower bound: ",lower_bound)
    print("Uper bound: ",upper_bound)
    print("Lower outliers:", lower_outliers)
    print("Upper outliers:", upper_outliers)

def find_Q1_Q2_Q3(data):
    data = np.array(data)

    q1 = np.percentile(data, 25)
    print("Q1 (25th percentile):", q1)

    q2 = np.percentile(data, 50)
    print("Q2 (50th percentile - Median):", q2)

    q3 = np.percentile(data, 75)
    print("Q3 (75th percentile):", q3)

def find_mode(arr):
    data = np.array(arr)
    unique_values, counts = np.unique(data, return_counts=True)
    max_count = np.max(counts)
    mode = unique_values[counts == max_count]
    print("mode: ",mode)
    return mode

def find_mean(arr:list):
    total = 0
    for num in arr:
        total+=num
    mean = total/len(arr)
    print("total number: ",total)
    print("mean number: ",mean)
    return mean

def find_meian(arr:list):
    arr_len = len(arr)
    if(arr_len%2 == 0):
        fist_indexForMedian = int(arr_len/2) 
        second_indexForMedian = int((arr_len/2)-1)
        median = float((arr[fist_indexForMedian]+arr[second_indexForMedian])/2)
        print("median number: ",median)
        return median
    else:
        indexForMedian = int((arr_len/2))
        median = int(arr[indexForMedian])
        print("median number: ",median)
        return median

root()
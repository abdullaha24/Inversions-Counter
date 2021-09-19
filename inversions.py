# inversions.py
# Author: Abdullah Asif

def mergesort(arr):
    inversions = 0 
    mid = len(arr) // 2

    if len(arr) <= 1:
        return 0 

    left_side = arr[:mid]
    right_side = arr[mid:]

    inversions += mergesort(left_side)
    inversions += mergesort(right_side)
    inversions += merge(arr, left_side, right_side)

    return inversions 

def merge(arr, left, right):
    inversions = 0
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1 
        elif left[i] > right[j]:
            arr[k] = right[j]
            j += 1
            inversions += len(left) - i 
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return inversions 

def read_ints(file):
    arr = list()
    input_file = open(file, 'r')
    for line in input_file:
        arr.append(int(line))
    input_file.close()

    return arr 

def main():
    arr = read_ints('IntegerArray.txt')
    inversions = mergesort(arr)
    print('Inversions:', inversions) 

if __name__ == '__main__':
    main()
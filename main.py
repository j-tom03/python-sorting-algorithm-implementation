import random

#################### Bubble Sort ####################
def bubble_sort(arr):
    n = len(arr) # Saves computation on each iteration
    comparison_count = 0 # To count the number of comparisons
    for i in range(n):
        for j in range(n-i-1): # n-i-1 because the last i elements are already sorted
            comparison_count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap the elements if out of order

    print(f"Bubble Sort - Comparison count: {comparison_count}")
    return arr

#################### Insertion Sort ####################
def insertion_sort(arr):
    sorted_arr = [] # To store the sorted array
    n = len(arr) # Saves computation on each iteration
    comparison_count = 0 # To count the number of comparisons
    for i in range(n):
        if i==0:
            sorted_arr.append(arr[i]) # Add the first element to the sorted array
        else:
            for j in range(len(sorted_arr)):
                comparison_count += 1
                if arr[i] < sorted_arr[j]:
                    sorted_arr.insert(j, arr[i]) # Insert the element at the correct position
                    break
            sorted_arr.append(arr[i]) # If the element is the largest, add it to the end
    
    print(f"Insertion Sort - Comparison count: {comparison_count}")
    return sorted_arr

#################### Merge Sort ####################
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

def merge(left, right):
    sorted_arr = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

def quick_sort(arr):
    pass

#################### Bogo Sort ####################
def bogo_sort(arr):
    attempts = 0
    random.shuffle(arr)
    attempts += 1
    while not is_sorted(arr):
        attempts += 1
        random.shuffle(arr)

    print(f"Bogo Sort - Attempts: {attempts}")
    return arr
    
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

#################### Main ####################
if __name__ == '__main__':
    arr = [5,3,4,2,6,7,8,9,1,0]
    print("Bubble Sort:")
    print(bubble_sort(arr))
    print("Insertion Sort:")
    print(insertion_sort(arr))
    print("Merge Sort:")
    #print(merge_sort(arr))

    print("Bogo Sort:")
    print(bogo_sort(arr))
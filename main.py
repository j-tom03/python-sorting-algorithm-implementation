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

if __name__ == '__main__':
    arr = [5,3,4,2,6,7,8,9,1,0]
    print("Bubble Sort:")
    print(bubble_sort(arr))
    print("Insertion Sort:")
    print(insertion_sort(arr))
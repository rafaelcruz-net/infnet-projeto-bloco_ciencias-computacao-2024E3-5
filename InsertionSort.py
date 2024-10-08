def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 10, 5, 50, 25, 5, 6, 7, 4]
print("Array original", arr)
print("Array ordenado com insertion sort", insertion_sort(arr))
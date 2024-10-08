def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if (arr[j] < arr[min_ind]):
                    min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

arr = [64, 25, 12, 22, 11, 5, 8, 1]
print("Array original", arr)
print("Array ordenado com selection sort", selection_sort(arr))
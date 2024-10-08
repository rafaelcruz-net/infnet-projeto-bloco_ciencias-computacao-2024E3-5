import random

def merge_sort(arr):
    if (len(arr) > 1):
        mid = len(arr) // 2
        
        L = arr[:mid]
        R = arr[mid:]

        # CHAMAMOS DE FORMA RECURSIVA O MERGE SORT, CASO PRECISE QUEBRAR MAIS SUBLISTA        
        merge_sort(L)
        merge_sort(R)

        i = 0
        j = 0
        k = 0

        # ORDENAMOS AS SUBLISTAS
        while i < len(L) and j < len(R):
            if (L[i] < R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        #JUNTAMOS A SUBLISTA A ESQUERDA
        while i < len(L): 
            arr[k] = L[i]
            i += 1
            k += 1
        
        #JUNTAMOS A SUBLISTA A DIREITA
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if (arr[j] < arr[min_ind]):
                    min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

def auto_sort(arr):
    n = len(arr)

    def is_nearly_sorted(arr):
        inversions = 0
        for i in range(1, len(arr)):
            if (arr[i] < arr[i-1]):
                inversions += 1
            if inversions > n // 10:
                return False
        return True
    
    if (n < 10):
        print ("Usando Insertion Sort para listas pequenas")
        return insertion_sort(arr)
    elif is_nearly_sorted(arr):
        print("Usando Insert Sort para listas quase ordenadas")
        return insertion_sort(arr)
    elif n < 100:
        print("Usando Selection Sort para listas de tamanho médio")
        return selection_sort(arr)
    else:
        print("Usando Merge Sort para listas grandes")
        return merge_sort(arr)
    

arr=random.sample(range(200),101)
    

print("Array original", arr)
sorted_arr = auto_sort(arr)
print("Array Ordernando", sorted_arr)


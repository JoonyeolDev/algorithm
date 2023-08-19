def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

test_array = [5, 3, 8, 4, 2]
print(test_array)
sorted_array = insertion_sort(test_array)
print(sorted_array)
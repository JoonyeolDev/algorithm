def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(middle)
    return quick_sort(left) + middle + quick_sort(right)

test_array = [5, 3, 8, 4, 2]
print(test_array)
sorted_array = quick_sort(test_array)
print(sorted_array)
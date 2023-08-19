def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
        print(result,left_idx,right_idx)
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1
        print(result,left_idx)
    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1
        print(result,right_idx)
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

test_array = [5, 3, 8, 4, 2]
sorted_array = merge_sort(test_array)
print(sorted_array)

test_array.sort()
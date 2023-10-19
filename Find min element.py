def find_min(arr):
    if not arr:
        return None
    min_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element

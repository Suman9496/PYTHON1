def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return its index
    return -1  # Element not found


# Usage example
if __name__ == "__main__":
    my_list = [5, 2, 9, 1, 5, 6]
    target_element = 9
    result = linear_search(my_list, target_element)

    if result != -1:
        print(f"Element {target_element} found at index {result}.")
    else:
        print(f"Element {target_element} not found in the list.")

def binary_search(list, target):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2

    if list[mid] == target:
      return mid
    elif list[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1


# Example usage:

list = [1, 3, 5, 7, 9]
target = 5

index = binary_search(list, target)

if index != -1:
  print("The target element is at index", index)
else:
  print("The target element is not in the list")

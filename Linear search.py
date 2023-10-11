def linear_search(list, target):
  for i in range(len(list)):
    if list[i] == target:
      return i
  return -1


# Example usage:

list = [1, 5, 3, 2, 4]
target = 3

index = linear_search(list, target)

if index != -1:
  print("The target element is at index", index)
else:
  print("The target element is not in the list")

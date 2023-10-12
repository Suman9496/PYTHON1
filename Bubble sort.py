def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


# Example usage:

list[int] = [5, 3, 1, 2, 4]

sorted_list = bubble_sort()

print(sorted_list)



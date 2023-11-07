def bubble_sort_students(student_scores):
    n = len(student_scores)

    for i in range(n - 1):
        # Flag to optimize if no swaps are needed in a pass
        swapped = False

        for j in range(0, n - i - 1):
            if student_scores[j][1] > student_scores[j + 1][1]:
                # Swap the students if their scores are out of order
                student_scores[j], student_scores[j + 1] = student_scores[j + 1], student_scores[j]
                swapped = True

        # If no swaps occurred in the last pass, the list is already sorted
        if not swapped:
            break


# Example usage
if __name__ == "__main__":
    students = [("Alice", 85), ("Bob", 72), ("Charlie", 95), ("David", 68)]

    print("Unsorted list of students:")
    for student in students:
        print(student[0], "-", student[1])

    bubble_sort_students(students)

    print("\nSorted list of students by exam scores (ascending order):")
    for student in students:
        print(student[0], "-", student[1])

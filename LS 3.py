def linear_search_people(people, target_name):
    for i, person in enumerate(people):
        if person['name'] == target_name:
            return i  # Person found, return their index
    return -1  # Person not found


# Usage example
if __name__ == "__main__":
    people_list = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 22},
        {'name': 'David', 'age': 28},
    ]
    target_name = 'Charlie'

    result = linear_search_people(people_list, target_name)

    if result != -1:
        print(f"{target_name} found at index {result}.")
    else:
        print(f"{target_name} not found in the list.")

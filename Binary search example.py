def binary_search_phone_book(phone_book, target_name):
    left, right = 0, len(phone_book) - 1

    while left <= right:
        mid = (left + right) // 2
        current_name, phone_number = phone_book[mid]

        if current_name == target_name:
            return phone_number  # Person found, return their phone number
        elif current_name < target_name:
            left = mid + 1
        else:
            right = mid - 1

    return None  # Person not found


# Example usage
if __name__ == "__main__":
    phone_book = [("Alia", "5552321234"), ("Bro", "5551235678"), ("Sharma", "5551237890"), ("Dharma", "5551234321")]
    target_name = "Sharma"

    phone_number = binary_search_phone_book(phone_book, target_name)

    if phone_number is not None:
        print(f"{target_name}'s phone number: {phone_number}")
    else:
        print(f"{target_name} not found in the phone book.")

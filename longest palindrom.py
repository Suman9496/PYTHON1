def is_palindrome(s):
    return s == s[::-1]


def longest_palindromic_substring(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    longest_palindrome = ""

    for word in words:
        for i in range(len(word)):
            for j in range(i, len(word)):
                substring = word[i:j + 1]
                if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

    return longest_palindrome


if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    result = longest_palindromic_substring(user_input)

    if result:
        print("Longest palindromic substring:", result)
    else:
        print("No palindromic substring found in the sentence.")

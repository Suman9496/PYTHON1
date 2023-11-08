roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def convert_arabic_to_roman(arabic_number):
    if arabic_number <= 0 or arabic_number > 3999:
        raise ValueError("Invalid Arabic number. Must be between 1 and 3999.")

    roman_number = ""
    for value, numeral in enumerate(roman_numerals[::-1]):
        while arabic_number >= value:
            roman_number += numeral
            arabic_number -= value

    return roman_number


def convert_roman_to_arabic(roman_number):
    roman_numerals_dict = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
                           "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}
    arabic_number = 0

    for i in range(len(roman_number)):
        current_value = roman_numerals_dict[roman_number[i]]
        next_value = 0 if i == len(roman_number) - 1 else roman_numerals_dict[roman_number[i + 1]]

        if current_value < next_value:
            arabic_number -= current_value
        else:
            arabic_number += current_value

    return arabic_number


print(convert_arabic_to_roman(123))
print(convert_roman_to_arabic("MCXXI"))

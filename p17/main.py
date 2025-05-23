mappings = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def number_letter_counts(number: int) -> int:
    thousands, hundreds, tens, units = [int(d) for d in f"{number:0>4}"]
    thousands_hundreds = []
    tens_units = []

    if thousands:
        thousands_hundreds.extend([mappings[thousands], mappings[1000]])

    if hundreds:
        thousands_hundreds.extend([mappings[hundreds], mappings[100]])
    
    if tens == 1: # 11-19
        tens_units.extend([mappings[tens * 10 + units]])
    else:
        if tens:
            tens_units.extend([mappings[tens * 10]])
        if units:
            tens_units.extend([mappings[units]])

    num_string = f'{" ".join(thousands_hundreds)}{" and " if thousands_hundreds and tens_units else ""}{" ".join(tens_units)}'
    #print (num_string)
    return len(num_string.replace(" ",""))



assert number_letter_counts(1) == 3
assert number_letter_counts(2) == 3
assert number_letter_counts(3) == 5
assert number_letter_counts(4) == 4
assert number_letter_counts(5) == 4
assert sum([number_letter_counts(num) for num in range(1,6)]) == 19
assert number_letter_counts(342) == 23
assert number_letter_counts(115) == 20

# Answer
print(sum([number_letter_counts(num) for num in range(1,1001)]))
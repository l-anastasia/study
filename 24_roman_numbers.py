# create a function that takes a number in roman system
# and tranfer it to arabic system

def roman_to_arabic(roman_str):
    transfer_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }
    arabic = 0

    if "IIII" in roman_str \
        or "VV" in roman_str \
        or "XXXX" in roman_str \
        or "LL" in roman_str \
        or "CCCC" in roman_str \
        or "DD" in roman_str:
            return ("You wrote your number wrong, try again")

    for i in range(len(roman_str) - 1):
        if roman_str[i] not in transfer_dict or \
            roman_str[i + 1] not in transfer_dict:
           return "This is not a number in roman system, try again"

        if transfer_dict[roman_str[i]] >= transfer_dict[roman_str[i + 1]]:
            if i == 0:
                arabic += (transfer_dict[roman_str[i]]
                        + transfer_dict[roman_str[i + 1]])
            else:
                arabic += transfer_dict[roman_str[i + 1]]
        else:
            arabic += (transfer_dict[roman_str[i + 1]]
                    - transfer_dict[roman_str[i]])
    return arabic

# testing
print(roman_to_arabic("XV"))
print(roman_to_arabic("XCII"))
print(roman_to_arabic("CMLVI"))
print(roman_to_arabic("XAII"))
print(roman_to_arabic("XXAII"))
print(roman_to_arabic("XXXXII"))

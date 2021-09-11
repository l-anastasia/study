# create a function, that takes a string
# and returns how many vowels in it


def counting_vowels(string):
    result = 0
    for letter in string.lower():
        if letter in 'aeiou':
            result += 1
    return result


def counting_vowels_comprehension(string):
    return sum([1 for letter in string.lower() if letter in 'aeiou'])


# testing
print(counting_vowels('abcd'))
print(counting_vowels('garden'))
print(counting_vowels('SunRiSe'))

print(counting_vowels_comprehension('abcd'))
print(counting_vowels_comprehension('garden'))
print(counting_vowels_comprehension('SunRiSe'))

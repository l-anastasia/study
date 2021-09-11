# create a function that takes a sequence,
# and returns: 1 if its strictly increasing, -1 - if strictly decreasing, 0 if neither


def check_sequence(lst):
    counter = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            counter += 1
        if lst[i] == lst[i-1]:
            return 0

    if counter == len(lst) -1:
        return 1
    if 0 < counter < len(lst) - 1:
        return 0
    return -1


def check_sequence_sort(lst):
    if sorted(set(lst)) == lst:
        return 1
    if sorted(set(lst), reverse=True) == lst:
        return -1
    return 0

# testing
print(check_sequence([1, 2, 3]))
print(check_sequence([3, 2, 1]))
print(check_sequence([1, 2, 1, 8, 7]))
print(check_sequence([1, 1, 3, 5]))

print(check_sequence_sort([1, 2, 3]))
print(check_sequence_sort([3, 2, 1]))
print(check_sequence_sort([1, 2, 1, 8, 7]))
print(check_sequence_sort([1, 1, 3, 5]))

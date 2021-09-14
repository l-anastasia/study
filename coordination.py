# create a function that takes a list of coordinates for points
# and defines how many rectangles theese points form

def rectangles(data):
    data_set = set()
    for item1 in data:
        for item2 in data:
            if item1[0] == item2[0] and item1 != item2:
                for item3 in data:
                    if item3[1] == item1[1] and item3 != item1:
                        for item4 in data:
                            if item4[0] == item3[0] and \
                                item4[1] == item2[1] and \
                                item4 != item3 != item2:
                                data_set.add(frozenset([ \
                                    item1, item2, item3, item4]))
    return len(data_set)

# testing
print(rectangles([(1, 1), (1, -1), (-2, -1), (-2, 1)])) # 1
print(rectangles([(1, 1), (1, -1), (-2, -1), (-2, 1), \
    (1, 2), (3, 1), (3, 2)])) # 2
print(rectangles([(1, 1), (1, -1), (-2, -1), (-2, 1), \
    (1, 2), (3, 1), (3, 2), (1, -4), (3, -4)])) # 4

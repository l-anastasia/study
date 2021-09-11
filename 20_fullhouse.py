# create a function, that takes a "hand" (5 cards)
# and defines if its fullhouse - 2 and 3 cards with the same suit - or not
# returns True or False accordingly


def is_full_house(*args):
    card_dict = {}
    for card in args:
        if card not in card_dict.keys():
            card_dict[card] = 1
        else:
            card_dict[card] += 1
    if (2 in card_dict.values()) and (3 in card_dict.values()):
        return True
    return False

# testing
print(is_full_house('A','A','J','J','J'))
print(is_full_house('A','A','10','J','J'))
print(is_full_house('2','3','10','5','J'))

def is_full_house_comprehension(*args):
    return all([args.count(item) >= 2 for item in args])

print(is_full_house_comprehension('A','A','J','J','J'))
print(is_full_house_comprehension('A','A','10','J','J'))
print(is_full_house_comprehension('2','3','10','5','J'))

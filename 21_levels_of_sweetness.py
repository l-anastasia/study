# create a function that takes instances of IceCream class
# and returns the sweetest of them
# every flavor has its own level of sweetness


class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles
        flavors_dict = {
            "Plain":0,
            "Vanilla":5,
            "ChocolateChip":5,
            "Strawberry":10,
            "Chocolate":10
            }

        self.flavor_sweetness = flavors_dict[self.flavor]

    def sweetest_icecream(lst):
        sweetness = []
        for icecream in lst:
            sweetness.append(icecream.flavor_sweetness + icecream.sprinkles)
        return max(sweetness)



def sweetest_icecream_comprehension(lst):
    return max([(icecream.flavor_sweetness + icecream.sprinkles) for icecream in lst])

# testing
ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)

print(IceCream.sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))
print(sweetest_icecream_comprehension([ice1, ice2, ice3, ice4, ice5]))

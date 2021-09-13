# create class Pagination that processes the data (list)
# pagination is used for separate the list to so-called pages
# __init__ takes two parameters: items - the data
# and page_size - the amount of string visible on one page
# the functionality required is bellow


import math
import string


class Pagination:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.page = 1
        self.the_last_page = math.ceil((len(self.items) - 1) / self.page_size)

    def get_visible_items(self):
        first = self.page_size * (self.page - 1)
        last = self.page_size * self.page
        result = self.items[first:last]
        print(result)
        return result

    def prev_page(self):
        self.page -= 1
        return self

    def next_page(self):
        self.page += 1
        return self

    def first_page(self):
        self.page = 1
        return self

    def last_page(self):
        self.page = self.the_last_page
        return self

    def go_to_page(self, new_page):
        if new_page > self.the_last_page:
            self.page = self.the_last_page
        if new_page < 1:
            self.page = 1
        else:
            self.page = new_page
        return self

    def get_current_page(self):
        print(self.page)
        return self.page

    def get_page_size(self):
        print(self.page_size)
        return self.page_size

    def get_items(self):
        print(self.items)
        return self.items

#testing
data = list(string.ascii_lowercase)
p = Pagination(data, 4)

p.get_items()
p.get_visible_items()
p.next_page()
p.get_visible_items()
p.last_page()
p.get_visible_items()

p.prev_page().next_page()
p.get_visible_items()

p.go_to_page(2).next_page()
p.get_visible_items()

p.last_page().prev_page()
p.get_visible_items()

class Inventory():
    def __init__(self):
        self.items = []

    def add(self, item):
        # append new item
        self.items.append(item)

    def remove(self, item_name):
        # remove item
        item = self.find(item_name)
        self.items.remove(item)
        # return the moved item
        return item

    def find(self, item_name):
        # find item by item_name
        for item in self.items:
            if item.name == item_name:
                # return the whole item
                return item
        # not found
        return 0

    def __str__(self):
        if len(self.items) == 0:
            # empty
            s = "Your inventory is empty.\n"
        else:
            # get all the items
            s = ""
            for item in self.items:
                s += f"{item.name}: {item.description}\n"
        return s
class Item():
    def __init__(self, name, description):
        # name and description
        self.name = name
        self.description = description

    def __str__(self):
        # print item's name and description
        return f"{self.name}: {self.description}"
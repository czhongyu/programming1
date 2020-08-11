from inventory import Inventory


class Room(object):
    """
    Representation of a room in Adventure
    """

    def __init__(self, id, name, description):
        """
        Initializes a Room
        """
        self.id = id
        self.name = name
        self.description = description
        self.route = []
        self.visited = 0
        self.inventory = Inventory()

    def add_route(self, direction, room_id, item=""):
        """
        Adds a given direction and the connected room to our room object.
        """
        # TODO: implement (hint: you might need to add some lines to init)
        if item == "":
            # not item required
            self.route.append([direction, room_id])
        else:
            # required item
            self.route.append([direction, room_id, item])

    def is_connected(self, direction):
        """
        Checks whether the given direction has a connection from a room.
        Returns a boolean.
        """
        # TODO: implement
        i = 0
        routes = []
        # get all the routes with this direction
        for i in range(len(self.route)):
            if self.route[i][0] == direction:
                routes.append(i)
            i = i + 1

        return routes

    def __str__(self):
        if self.visited and self.route[0][0] != "FORCED":
            # visited and not a forced movement
            return self.name
        else:
            # not visited or a forced movement
            self.visited = 1
            return self.description


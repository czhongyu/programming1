from room import Room
from item import Item
from inventory import Inventory


class Adventure():
    """
    This is your Adventure game class. It should contains
    necessary attributes and methods to setup and play
    Crowther's text based RPG Adventure.
    """

    def __init__(self, game):
        """
        Create rooms and items for the appropriate 'game' version.
        """
        self.rooms = self.load_rooms(f"data/{game}Rooms.txt")
        self.current_room = self.rooms[1]
        # use self.over to determine if the game if over
        self.over = 0
        self.load_items(f"data/{game}Items.txt")
        self.inventory = Inventory()
        # synonyms
        self.synonyms = {}
        self.load_synonyms("data/SmallSynonyms.txt")

    def load_rooms(self, filename):
        """
        Load rooms from filename.
        Returns a dictionary of 'id' : Room objects.
        """
        # First we parse all the data we need to create the rooms with.
        # All parsed lines of data are saved to rooms_data.
        rooms_data = []
        with open(filename, "r") as f:
            room_data = []
            for line in f:
                # When there is no blank newline it means there's still data.
                if not line == "\n":
                    room_data.append(line.strip())
                # A blank newline signals all data of a single room is parsed.
                else:
                    rooms_data.append(room_data)
                    room_data = []
        # Append a final time, because the files do not end on a blank newline.
        rooms_data.append(room_data)

        # Create room objects for each set of data we just parsed.
        rooms = {}
        for room_data in rooms_data:
            id = int(room_data[0])
            name = room_data[1]
            description = room_data[2]

            # Initialize a room object and put it in a dictionary with its
            # id as key.
            room = Room(id, name, description)
            rooms[id] = room

        # Add routes to each room we've created with the data from each set
        # we have parsed earlier.
        for room_data in rooms_data:
            id = int(room_data[0])
            # We split to connections into a direction and a room_id.
            connections = room_data[4:]
            connections = [connection.split() for connection in connections]
            # Here we get the current room object that we'll add routes to.
            room = rooms[id]
            for connection, target_room_id in connections:
                # TODO add routes to a room (hint: use the add route method)
                # split id and item
                idanditem = target_room_id.split('/', 1)
                if len(idanditem) < 2:
                    room.add_route(connection, target_room_id)
                else:
                    room.add_route(connection, idanditem[0], idanditem[1])
            rooms[id] = room

        return rooms

    def load_items(self, filename):
        # load items, just like the process of loading rooms
        items_data = []
        with open(filename, 'r') as f:
            item_data = []
            for line in f:
                if line != "\n":
                    item_data.append(line.strip())
                else:
                    items_data.append(item_data)
                    item_data = []
        items_data.append(item_data)

        # add items into inventory
        for item_data in items_data:
            self.rooms[int(item_data[2])].inventory.add(Item(item_data[0], item_data[1]))

    def game_over(self):
        """
        Check if the game is over.
        Returns a boolean.
        """
        # TODO: Define the game over condition for Adventure.
        # use self.over to determine if the game if over
        return self.over

    def move(self, direction):
        """
        Moves to a different room in the specified direction.
        """
        # TODO: Update the current room to a connected direction.
        # get route id list
        route_ids = self.current_room.is_connected(direction)
        # check route id one by one
        for route_id in route_ids:
            route = self.current_room.route[int(route_id)]
            room_id = int(route[1])
            # victory
            if room_id == 0:
                self.over = 1
                return

            if len(route) == 3:
                # item required
                item_name = route[2]
                if self.inventory.find(item_name):
                    # contain this item
                    self.current_room = self.rooms[room_id]
                    return
            else:
                # do not required item
                self.current_room = self.rooms[room_id]
                return
            # do not have the required item, check the next route

    def play(self):
        """
        Play an Adventure game
        """
        print(f"Welcome, to the Adventure games.\n"
              "May the randomly generated numbers be ever in your favour.\n")

        # Prompt the user for commands until they've won the game.
        while not self.game_over():
            # current_room name or description
            print(self.current_room)
            # current_room inventory
            if len(self.current_room.inventory.items) > 0:
                print(self.current_room.inventory, end="")
            # force movement
            if self.current_room.route[0][0] == "FORCED":
                self.move("FORCED")
                continue
            # prompt for input
            command = input("> ")
            # case insensitive
            command = command.upper()
            # split command and item name
            commands = command.split(' ', 1)
            if len(commands) == 2:
                command = commands[0]
                item_name = commands[1]
            else:
                item_name = ""
            # transform synonyms into normal command
            if command in self.synonyms:
                command = self.synonyms[command]
            # Check if the command is a movement or not.
            if len(self.current_room.is_connected(command)):
                # TODO: Perform a move.
                # the routes exist
                self.move(command)
            else:
                # TODO: Command not implemented!
                if command == "HELP":
                    self.help()
                elif command == "QUIT":
                    self.quit()
                elif command == "LOOK":
                    self.look()
                elif command == "INVENTORY":
                    print(self.inventory, end="")
                elif item_name != "":
                    if command == "TAKE":
                        self.take(item_name)
                    elif command == "DROP":
                        self.drop(item_name)
                    else:
                        self.invalid()
                else:
                    self.invalid()

    def help(self):
        # print help messages
        print("You can move by typing directions such as EAST/WEST/IN/OUT")
        print("QUIT quits the game.")
        print("HELP prints instructions for the game.")
        print("INVENTORY lists the item in your inventory.")
        print("LOOK lists the complete description of the room and its contents.")
        print("TAKE <item> take item from the room.")
        print("DROP <item> drop item from your inventory.")

    def quit(self):
        # quit game
        self.over = 1
        print("Thanks for playing!")

    def look(self):
        # print description and inventory
        print(self.current_room.description)
        print(self.current_room.inventory, end="")

    def invalid(self):
        # invalid command
        print("Invalid command.")

    def take(self, name):
        # take item
        if self.current_room.inventory.find(name):
            # exist
            self.inventory.add(self.current_room.inventory.remove(name))
            print(f"{name} taken.")
        else:
            # not exist
            print("No such item.")

    def drop(self, name):
        # drop item
        if self.inventory.find(name):
            # exist
            self.current_room.inventory.add(self.inventory.remove(name))
            print(f"{name} dropped.")
        else:
            # not exist
            print("No such item.")

    def load_synonyms(self, filename):
        # load synonyms and save them in a dict
        with open(filename, 'r') as f:
            for line in f:
                synonyms = line.strip().split('=', 1)
                self.synonyms[synonyms[0]] = synonyms[1]


if __name__ == "__main__":
    adventure = Adventure("Crowther")
    adventure.play()
    # # should move to the 'room 2' object
    # adventure.move("WEST")
    # # should print room 2: "End of road"
    # print(adventure.current_room)
    # # should move to the 'room 1' object
    # adventure.move("DOWN")
    # # should move to the 'room 3' object
    # adventure.move("IN")
    # # should print room 3: "Inside building"
    # print(adventure.current_room)
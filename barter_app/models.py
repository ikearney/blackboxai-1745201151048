class User:
    def __init__(self, user_id, name, location):
        """
        Initialize a User instance.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): Name of the user.
            location (str): Location of the user.
        """
        self.user_id = user_id
        self.name = name
        self.location = location
        self.items_offered = []

    def add_item(self, item):
        """
        Add an item to the user's offered items.

        Args:
            item (Item): The item to add.
        """
        self.items_offered.append(item)

    def remove_item(self, item_name):
        """
        Remove an item from the user's offered items by name.

        Args:
            item_name (str): The name of the item to remove.
        """
        self.items_offered = [item for item in self.items_offered if item.name != item_name]

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Location: {self.location}"

    def __repr__(self):
        return self.__str__()

class Item:
    def __init__(self, item_id, name, description, owner):
        """
        Initialize an Item instance.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            description (str): Description of the item.
            owner (User): The owner of the item.
        """
        self.item_id = item_id
        self.name = name
        self.description = description
        self.owner = owner

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Owner: {self.owner.name}"

    def __repr__(self):
        return self.__str__()

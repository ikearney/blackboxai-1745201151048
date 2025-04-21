import logging
from barter_app.models import User, Item

class BarterApp:
    def __init__(self):
        self.users = {}
        self.items = {}
        self.next_user_id = 1
        self.next_item_id = 1
        self.logger = logging.getLogger('BarterApp')

    def register_user(self, name, location):
        user_id = self.next_user_id
        new_user = User(user_id, name, location)
        self.users[user_id] = new_user
        self.next_user_id += 1
        self.logger.info(f"User '{name}' registered successfully with ID: {user_id}")
        return new_user

    def add_item(self, user_id, name, description):
        if user_id in self.users:
            item_id = self.next_item_id
            new_item = Item(item_id, name, description, self.users[user_id])
            self.items[item_id] = new_item
            self.users[user_id].add_item(new_item)
            self.next_item_id += 1
            self.logger.info(f"Item '{name}' added for user ID {user_id}")
            return new_item
        else:
            self.logger.error("User not found.")
            return None

    def remove_item(self, user_id, item_name):
        if user_id in self.users:
            user = self.users[user_id]
            user.remove_item(item_name)
            # Also remove from global items dictionary
            items_to_remove = [item_id for item_id, item in self.items.items() if item.name == item_name and item.owner.user_id == user_id]
            for item_id in items_to_remove:
                del self.items[item_id]
            self.logger.info(f"Item '{item_name}' removed for user ID {user_id}")
        else:
            self.logger.error("User not found.")

    def search_items(self, query):
        results = [item for item in self.items.values() if query.lower() in item.name.lower() or query.lower() in item.description.lower()]
        if results:
            self.logger.info("Search results:")
            for item in results:
                self.logger.info(str(item))
        else:
            self.logger.info("No items found matching your query.")

    def find_items_by_user(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            if user.items_offered:
                self.logger.info(f"Items offered by {user.name}:")
                for item in user.items_offered:
                    self.logger.info(str(item))
            else:
                self.logger.info(f"{user.name} has not offered any items yet.")
        else:
            self.logger.error("User not found.")

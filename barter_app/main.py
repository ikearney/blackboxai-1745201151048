import argparse
from barter_app.app import BarterApp
from barter_app.utils import setup_logging

def main():
    setup_logging()
    app = BarterApp()

    parser = argparse.ArgumentParser(description="Barter App CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Register user command
    register_parser = subparsers.add_parser('register', help='Register a new user')
    register_parser.add_argument('name', type=str, help='Name of the user')
    register_parser.add_argument('location', type=str, help='Location of the user')

    # Add item command
    add_parser = subparsers.add_parser('add', help='Add an item for a user')
    add_parser.add_argument('user_id', type=int, help='User ID')
    add_parser.add_argument('name', type=str, help='Name of the item')
    add_parser.add_argument('description', type=str, help='Description of the item')

    # Remove item command
    remove_parser = subparsers.add_parser('remove', help='Remove an item for a user')
    remove_parser.add_argument('user_id', type=int, help='User ID')
    remove_parser.add_argument('item_name', type=str, help='Name of the item to remove')

    # Search items command
    search_parser = subparsers.add_parser('search', help='Search items by query')
    search_parser.add_argument('query', type=str, help='Search query')

    # List items by user command
    list_parser = subparsers.add_parser('list', help='List items offered by a user')
    list_parser.add_argument('user_id', type=int, help='User ID')

    args = parser.parse_args()

    if args.command == 'register':
        user = app.register_user(args.name, args.location)
        print(f"User registered: {user}")

    elif args.command == 'add':
        item = app.add_item(args.user_id, args.name, args.description)
        if item:
            print(f"Item added: {item}")
        else:
            print("Failed to add item.")

    elif args.command == 'remove':
        app.remove_item(args.user_id, args.item_name)
        print(f"Item '{args.item_name}' removed for user ID {args.user_id}.")

    elif args.command == 'search':
        app.search_items(args.query)

    elif args.command == 'list':
        app.find_items_by_user(args.user_id)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

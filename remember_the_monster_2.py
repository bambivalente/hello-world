# make a list to hold onto our items
monster_list = []

def show_help():
    # print out instructions on how to use the app
    print("What do we need to remember?")
    print("""
Enter 'DONE' to stop adding items.
Enter HELP for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
    # print out the list
    print("Here's our monster list:")

    for item in monster_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    monster_list.append(new_item)
    print("Added {}. Monster list now has {} items.".format(new_item, len(monster_list)))

show_help()

while True:
    # ask for new items
    new_item = input("* ")

    # be able to quit the app
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()

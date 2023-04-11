known_users = ["Sai","Ram","Ganesh","Pranitha","Adya","Ashish","Manoj","Anudeep"]

while True:
    print("Hi! Travis, The Game of names with adding and removing users")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().upper()

        if remove == "Y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        else remove == "N":
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("I don't think I know you yet {}".format(name))
        add_me = input("Would you like to be added into the system (y/n)?: ").strip().lower()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("No Worries, see you around!")

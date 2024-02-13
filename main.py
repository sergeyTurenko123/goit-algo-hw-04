def parse_input(user_input):
    name, *args = user_input.split()
    name = name.strip().lower()
    return name, *args

def add_contact(args):
    name, phone = args
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0]: list_line[1].strip()})
    if name in lists:
        print("Contact exists. Re-record?")
    else:
        lists[name] = phone
        with open("name_phone.txt","w", encoding = "utf-8") as fh:
            for key, value in lists.items():
                fh.write(f'{key},{value}\n')
        return "Contact added."

def change_contact(args):
    name, phone = args
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0]: list_line[1].strip()})
    if name in lists:
        lists[name] = phone
        with open("name_phone.txt","w", encoding = "utf-8") as fh:
            for key, value in lists.items():
                fh.write(f'{key},{value}\n')
        return "Contact updated."
    else:
        print("Contact does not exist. Will you write it down?")
    

def show_phone(args):
    [name] = args
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0]: list_line[1].strip()})
    if name in lists:
        print(f"{name},{lists[name]}")
    else:
        print("Contact does not exist. Will you write it down?")
    

def show_all():
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0]: list_line[1].strip()})
    return lists

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

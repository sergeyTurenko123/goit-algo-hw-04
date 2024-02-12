def add_contact(args):
    name, phone = args
    with open("name_phone.txt","r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0].strip().lower(): list_line[1].strip()})
        if name in lists:
            print("Choose a different name")
        else:
            lists.update({name: phone})
    with open("name_phone.txt","w", encoding = "utf-8") as fh:
        for key, value in lists.items():
                fh.write(f'{key},{value}\n')
    return "Contact added."

def change_contact(args):
    name, phone = args
    with open("name_phone.txt","r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0].strip().lower(): list_line[1].strip()})
        if name in lists:
            lists[name] = phone
        else:
            lists.update({name: phone})
    with open("name_phone.txt","w", encoding = "utf-8") as fh:
        for key, value in lists.items():
                fh.write(f'{key},{value}\n')
    return "Contact updated."

def show_phone(args):
    name = args
    with open("name_phone.txt","r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0].strip().lower(): list_line[1].strip()})
    if name in lists:
        print(f"{name} {lists[name]}")
    else:
        print("There is no such name")
    return lists

def show_all():
    with open("name_phone.txt","r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0]: list_line[1].strip()})
    return lists
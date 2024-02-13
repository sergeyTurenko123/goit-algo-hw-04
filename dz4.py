# # Завдання №1:

# with open("path.txt","w") as fh:
#     fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\nSerg Turenko,2000")
  
# def total_salary(path):
#     try:
#         with open("path.txt","r") as fh:
#             lines = fh.readlines()
#             number = []
#         for line in lines:
#             line=line.split(",")
#             number.append(int(line[1]))
#         total = sum(number) 
#         average = total/len(number)
#         print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
#     except:
#         print("The file does not exist")
#     return (total, average)

# total, average = total_salary("path.txt")


#  # Завдання №2

# with open("get_cats_info.txt","w") as fh:
#     fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5\n")

# def get_cats_info(get_cats_info):
#     try:
#         with open('get_cats_info.txt', "r") as file:
#             lines = file.readlines()
#             lists = []
#         for line in lines:
#             list_line = line.split(",")
#             lists.append({"id": list_line[0], "name": list_line[1], "age": int(list_line[2].strip())})
#         return lists
#     except Exception:
#             print("The file does not exist")


# cats_info = get_cats_info("get_cats_info.txt")
# print(cats_info)
import re
with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
lists = {}
for line in lines:
    list_line = line.split(",")
    pattern = r"[\s\D]"
    repl = r""
    match = re.sub(pattern, repl, list_line[1])
    if len(match) == 10:
        match = f"+38{match}"
    elif len(match) == 11:
        match = f"+3{match}"
    elif len(match) == 12:
        match = f"+{match}"
    else:
        match = match
    lists.update({list_line[0]: match.strip()})

print(lists)



   
                


    

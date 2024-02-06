# Створення файлу

with open("path.txt","w") as fh:
    fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

# Завдання №1:
    
def total_salary(path):
    try:
        with open("path.txt","r") as fh:
            lines = fh.readlines()
            number = []
        for line in lines:
            line=line.split(",")
            number.append(int(line[1]))
        total = sum(number) 
        average = total/len(number)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except:
        print("The file does not exist")
    return (total, average)

total, average = total_salary("path.txt")



        
   
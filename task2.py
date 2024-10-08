#task 3
username = int(input("Enter the number of names: "))
namelist = []

for data in range(username):
    names = input("Enter name: ")
    namelist.append(names)
print(namelist)

lists = input("DO you want to remove an element?(by index or by name?): ")

if lists == "by index":
    namelist.pop()
elif lists == "by name":
    namelist.remove()

print(namelist)
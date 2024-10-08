#task 4
numlist =  int(input("enter numbers: "))
username = int(input("Enter the number of names: "))
numberlist = []
namelist = []

for data in range(numlist):
    number = int(input("Enter numbers: "))
    numberlist.append(number)

print(numberlist)

for i in range(username):
    names = input("Enter name: ")
    namelist.append(names)

print(namelist)

user = input("Do you want to sort or reverse? (yes or no): ")

if user == "yes":
    numberlist.sort()
    namelist.sort()
elif user == "no":
    numberlist.reverse()
    namelist.reverse()

print(numberlist)
print(namelist)
#task 1
usernum =  int(input("enter numbers: "))
numberlist = []

for data in range(usernum):
    num = int(input("numbers: "))
    numberlist.append(num)

user = input("do you want to add a number? (yes or no): ") 

if user == "yes":
    userdata = int(input("add number: "))
    numberlist.append(userdata)
print(numberlist)

#task 2
decision = input("Do you want to clear the list? (yes or no): ")

if decision == "yes":
    numberlist.clear()
elif decision == "no":
    print(numberlist)


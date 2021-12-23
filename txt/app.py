file = open("./app.txt", "w")
file.write("Hello World! \n")
file.write("Harlericho \n")
names = input("Enter your names: ")
file.write(names + "\n")
age = int(input("Enter your age: "))
file.write('age= % s'%age + "\n")
number = int(input("How many sports do you like? "))
list = []
for i in range(number):
    data = input("Enter your sports: ")
    list.append(data)
file.write('Sports= % s'%list + "\n")

file.close()
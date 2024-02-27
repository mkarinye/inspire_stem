#This  is a program to calculate increment
#Date : 26/02/2024
#Name : lawrence Jomo

salary = int(input("Enter employee's salary"))
if salary > 150000 :
    salary = salary *1.1
    print(salary)
elif salary > 100000 and salary <= 150000 :
    salary = salary * 1.15
    print(salary)
else :
    salary = salary * 1.3
    print(salary)
    
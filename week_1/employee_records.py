#This is a program that shows employee records
#Date : 21/02/2024
#Name : Lawrence Jomo

#Employees detail

n = input("Name : ")
a = input("Age ")
s = float(input("salary : "))
b = float(input("Bonus : "))

t = s + b

print("Employee's name :",n)
print("Employee's age :",a)
print("Employee's basic salary :",s)
print("Employee's bonus :",b)
print("Employee's total income :",t)

s2 = (130 / 100 * s)
t2 = s2 + b

print(" Employee's new bonus :",s2)
print("Employee's new total income :",t2)

b2 = b -5000
t2 = s2 + b2

print("Employee's new bonus :",b2)
print("Employee's final total income :",t2)




def print_name():
    print("My name is Lawrence Jomo")

#calling the function
print_name     

def print_details(name, age, id, gender):
    print("I am {0} ,{1} years old. My id no is {2} and gender is {3}".format(name, age, id, gender))

print_details("Lawrence Jomo","18","12776082","male")
print_details("Jane Forster", "24", "6788267", "female")

def sum_nums(x,y):
    return x + y
z = sum_nums(10,20)
print(z)

#product of numbers
def prod_nums(x,y):
    return x * y
print(prod_nums(5,16))


def print_odds(first_number, last_number):
    for i in range(first_number,last_number):
        print(i % 2)
print_odds(0,15)




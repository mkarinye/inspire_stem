# strings in python
#Date : 22/02/2024
# Name : Lawrence

city = "nairobi"

# convert to uppercase

print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[-1])
print(city[-2])
print(city[6])
print("\n") # prints a new line
print(city.upper())

name = "LAWRENCE JOMO"
print(name)
print(name.lower()) # covert string to lower case

town = "     Naivasha        "

print(town)
print("\t") # new tab

f_name = "Lawrence"
s_name = "Jomo"

full_name = f_name + s_name

print(full_name)

#replacing a character

fruit = "grape"

print(fruit.replace("O","Y"))

subject = "physics,sciences"

print(subject.split(":"))

age = 18

print("I am {} years old " . format(age))

height = 1.4

print("I am {0} years old and {1} meters tall" .format(age,height))

activity = "dancing"
print("My hobby is %s"%(activity))

height = 1.2334909
print("My height is %5.4f"% (height))

age = 18
print("My age is  %d "% (age))

name = "Lawrence Jomo"
print(len(name))

print(f"My full name is {name}")

school = "Engineering"
course = "Electrical"

print("I am studying {course} in the school of {school}".format(course = "medicine",school="human Scinces")) 
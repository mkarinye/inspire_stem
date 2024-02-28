#list 2
#Date : 28/02/2024
#Name : Jomo


friends = ["Lawrence","Mark","peter","Jane","Brendah"]
for friend in friends:
    print(friend)

    enemies = friend[:] # copy one list into another

    print(enemies)

    fruits = ["apple","grape","orange","melon"]
    #slice the list ie get part of the list
    print(fruits[0:3])

    del (fruits[0])
    print(fruits[0:3])

    squares = [ ] # initializes an empty list

    for x in range (0,11):
        squares.append(x**2)
    print(squares)
    


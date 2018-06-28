with open("text.txt", "r+") as file:

    #ex 1
    #print(file.read())

    #ex 2
    lines = file.readlines()
    print(lines[2])

    #ex 3
with open("text.txt", "a") as file:
    file.write("appended text")

#ex 4
with open("text.txt", "r+") as file:
    lines = file.readlines()
    print(lines[-2])
#ex 5
with open("text.txt", "r+") as file:
    list = file.readlines()
    print(list)
#ex 6 is same as previous one

#ex 7
with open("text.txt", "r+") as file:
    array = file.readines()
    print(array)

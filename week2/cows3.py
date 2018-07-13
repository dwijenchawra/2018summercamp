#FINDS THE GROUPS OF COWS AFTER INFINITE TIME



import collections

position = []
speed = []


def getinput():
    cowinput = input("Enter cow position and speed separated by whitespaces  Ex: 3 4 57 0.5:       ")
    #cowlist = [x for x in cowinput if x.isdigit() == True]
    cowinput = cowinput + " "
    cowlist = []
    appendedinfo = ""
    for i in cowinput:
        if i.isdigit() == True:
            appendedinfo = appendedinfo + i
        else:
            cowlist.append(int(appendedinfo))
            appendedinfo = ""
    return(cowlist)


def cows(x):
    for i in range(0, len(x)):
        if i % 2 != 0:
            speed.append(x[i])
        else:
            position.append(x[i])
    #once the lists are set then set the values of the cows
    #print(position)
    #print(speed)
    cowvalues = dict(zip(position, speed))
    cowvalues = collections.OrderedDict(sorted(cowvalues.items()))
    cowvalues = dict(cowvalues)
    return cowvalues
    #print(cowvalues)

cowdict = cows(getinput())

speeds = list(cowdict.values())
print(cowdict)


def rightmax(list):
    index = 0
    maximum = 0
    i = 0
    print("l"+str(list))
    while i < len(list):
        print("i: " + str(i))
        if list[i] >= maximum:
            maximum = list[i]
            del list[i]
            print("m"+str(maximum))
            i -= 1
        i += 1
    return list





def cow_eliminator(values):
    i = 0
    newnumberoflanes = 0
    while len(values) > 0:
        values = rightmax(values)
        i += 1
    return i








#   1 7 2 5 3 8 4 1 5 3 6 2
print("Number of lanes: " + str(cow_eliminator(speeds)))

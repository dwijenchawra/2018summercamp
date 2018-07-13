#BASICALLY COW PROBLEM EXCEPT ITS FINDING THE COW OSITIONS BASED ON THE TIME












import collections

speed = []
position = []


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

def cow_eliminator():
    values = list(cowdict.values())
    print(cowdict)
    values.append("end")
    length = len(values)
    print("loop begins here")
    i = 0
    while i < length - 1:
        print("loop: " + str(i))
        print("values: " + str(values))
        if i == length - 2:
            print("if")
            del values[-1]
            return(len(values))
        else:
            print("else")
            if values[i] > values[i + 1]:
                del values[i]
                i -= 1
                print(len(values))
                print(i)
                length = len(values)
        i += 1
#print(cow_eliminator())

def cow_time(time):
    speed = list(cowdict.values())
    position = list(cowdict.keys())
    print(speed)
    speed.append("end")
    length = len(speed)
    i = 0
    while i < length - 1:
        if i == length - 2:
            del speed[-1]
            return(len(speed))
        else:
            if speed[i] * time + position[i] >= speed[i + 1] * time + position[i + 1]:
                del speed[i]
                del position[i]
                i -= 1
                print(i)
                length = len(speed)
        i += 1


print("groups: " + str(cow_time()))

#THE BOOKSHELF PROBLEM

#sort list by greatest to least
#then get the first four books and put them in that BOOKSHELF
#take next four
#every fourth number (index 0, 4, 8, etc.) is the shelf number
def getinput():
    bookinput = input("Enter book height separated by spaces:      ")
    bookinput = bookinput + " "
    booklist = []
    appendedinfo = ""
    for i in bookinput:
        if i.isdigit() == True:
            appendedinfo = appendedinfo + i
        else:
            booklist.append(int(appendedinfo))
            appendedinfo = ""
    return(booklist)

booklist = getinput()

def shelver(booklist):
    booklist = sorted(booklist, reverse = True)
    shelves = []
    i = 0
    while i < len(booklist):
        if booklist[i] in shelves:
            shelves.append(booklist[i] + 1)
        else:
            shelves.append(booklist[i])
        i += 4
    return shelves

def cost(list):
    finalcost = 0
    for i in list:
        finalcost += i
    return finalcost


print(cost(shelver(booklist)))

class LinkedList:
    def __init__(self, value, child):
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value) + ", "+str(self.child)


    def addtolist(self,integer):
        if self.child == None:
            self.child = LinkedList(integer, None)
        else:
            self.child.addtolist(integer)


    def removefromlist(self, index):
        self.removefromlist_executer(index, 0)

    def removefromlist_executer(self, index, count):
        if count == index - 1:
            self.child = self.child.child
        else:
            self.child.removefromlist_executer(index, count + 1)


    def insertatindex(self, index, value):
        self.insertatindex_executer(index, value, 0)

    def insertatindex_executer(self, index, value, count):
        if count == index - 1:
            temp = self.child
            self.child = LinkedList(value, temp)
        else:
            self.child.insertatindex_executer(index, value, count + 1)
    def getindex(self, value):
        return self.getindex_executer(value, 0)

    def getindex_executer(self, value, count):
        temp = self.value
        if temp != value:
            return self.child.getindex_executer(value, count + 1)
        else:
            return count


    def nextoccurring(self, value):
        return self.nextoccurring_executer(value, 0, 0)

    def nextoccurring_executer(self, value, count, counter):
        temp = self.value
        if temp != value:
            return self.child.nextoccurring_executer(value, count + 1, counter)
        elif temp == value and counter == 0:
            return self.child.nextoccurring_executer(value, count + 1, counter + 1)
        else:
            return count


def toLinkList(array):
    if len(array) == 1:
        return LinkedList(array[0], child=None)
    else:
        return LinkedList(array[0], toLinkList(array[1:]))


x = toLinkList([1,2,3,4,5,56,54,5])
x.removefromlist(6)
x.insertatindex(5, 912836)
print(x.getindex(912836))
print(x.nextoccurring(5))
print(x)

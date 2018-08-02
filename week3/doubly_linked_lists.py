class DoubleLinkedList:
    def __init__(self, parent, value, child):
        self.parent = parent
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value) + ", " + str(self.child)

    def addParents(self):
        print("self.child:  " + str(self.child))
        #print("self.parent:  " + str(self.parent))
        if self.child == None:
            return
        else:
            self.child.parent = self
            self.child.addParents()


def toLinkList(list):
    if len(list) == 1:
        return DoubleLinkedList(None, list[0], None)
    else:
        return DoubleLinkedList(None, list[0], toLinkList(list[1:]))






x = toLinkList([1,2,3,4,5,56,54,32])
x.addParents()
#x.removefromlist(6)
#x.insertatindex(5, 912836)
#print(x.getindex(912836))
print(x)
print(x.child.child.child.parent.value)

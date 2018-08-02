nodes = "a b c d e f"
edges = "ab fe bc de" #these are the connections between nodes
lengths = "401 8 24 3" #lengths of the edges, respectively

def splitter(string, length):
    i = 0
    list = []
    while i <= len(string)-1:
        list.append(string[i:i+length])
        i += length+1
    return list

def lensplitter(lengths):
    lengths = lengths + " "
    lengthlist = []
    appendedinfo = ""
    for i in lengths:
        if i.isdigit() == True:
            appendedinfo = appendedinfo + i
        else:
            lengthlist.append(int(appendedinfo))
            appendedinfo = ""
    return(lengthlist)
nodeslist = splitter(nodes, 1)
edgelist = splitter(edges, 2)
lengthlist = lensplitter(lengths)

def edgefinder(node, list):
    #list has pairs of letters called edges
    connected = []
    for i in list:
        if node == i[0]:
            if i[1] not in connected:
                connected.append(i[1])
        elif node == i[1]:
            if i[0] not in connected:
                connected.append(i[0])
    return connected
#edgefinder("b", edgelist)

def equals(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

def connections(nodes, edges):
    discoverednodes = []
    discoverednodes.append(nodes[0])
    return equals(nodes.sort(), connections_exec(edges, 0, discoverednodes).sort())

def connections_exec(edges, counter, discoverednodes):
    if counter >= len(discoverednodes):
        return discoverednodes
    else:
        temp = edgefinder(discoverednodes[counter], edges)
        for i in range(len(temp)):
            if temp[i] not in discoverednodes:
                discoverednodes.append(temp[i])
        return connections_exec(edges, counter+1, discoverednodes)
print(connections(nodeslist, edgelist))

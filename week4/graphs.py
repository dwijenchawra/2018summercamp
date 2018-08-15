#djikstra's algorithm

nodes = "a b c d e f"
edges = "ab fe bc de cd" #these are the connections between nodes
lengths = "401 8 24 3 39" #lengths of the edges, respectively

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


def equals(list1, list2):
    list1.sort()
    list2.sort()
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
    return equals(nodes, connections_exec(edges, 0, discoverednodes))

def connections_exec(edges, counter, discoverednodes):
    if counter >= len(discoverednodes):
        return discoverednodes
    else:
        temp = edgefinder(discoverednodes[counter], edges)
        for i in range(len(temp)):
            if temp[i] not in discoverednodes:
                discoverednodes.append(temp[i])
        return connections_exec(edges, counter+1, discoverednodes)


def connections2( nodes, edges, lengths, start, end):
    discoverednodes = []
    discoverednodes.append(start)
    discoverednodes = connections_exec(edges, 0, discoverednodes)
    return end in discoverednodes

def edgefinder2(node, edges, lengths):
    #list has pairs of letters called edges
    connected = []
    nodevalue = []
    for i in range(len(edges)):
        if node == edges[i][0]:
            if edges[i][1] not in connected:
                connected.append(edges[i][1])
                nodevalue.append(lengths[i])
        elif node == edges[i][1]:
            if edges[i][0] not in connected:
                connected.append(edges[i][0])
                nodevalue.append(lengths[i])
    final = [connected, nodevalue]
    return final
print(edgefinder2("b", edgelist, lengthlist))

def zipper(list1, list2):
    return [list(a) for a in zip(list1, list2)]

def shortestpath(nodes, edges, lengths, start, end):
    discoverednodes = []
    discoverednodes.append(start)
    if connections2(nodes, edges, lengths, start, end):
        return shortestpath_exec(nodes, edges, lengths, start, end, start, 0, discoverednodes)
    else:
        return -1

def shortestpath_exec(nodes, edges, lengths, start, end, currentnode, counter, discoverednodes):
    if equals(discoverednodes, nodes) and counter == len(discoverednodes):
        return -1 #CHANGE TO VALUE OF END NODE
    else:
        temp = edgefinder2(currentnode, edges, lengthlist)
        print(temp)
        zipper(temp[0], temp[1])
        # expanding b: bc ba be
        # update discovered nodes by adding newly discovered nodes and
        # updating new values for shortest path
        return shortestpath_exec(nodes, edges, lengths, start, end, currentnode, counter+1, discoverednodes)

print(shortestpath(nodeslist, edgelist, lengthlist, "b", "e"))

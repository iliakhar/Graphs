
N1 = 0

class Edge:
    def __init__(self, vertex1, vertex2, lenth):
        self.v1 = vertex1
        self.v2 = vertex2
        self.lenth = lenth

def printGraph(graph, columnCount = 1):
    for i in range(len(graph)):
        print(graph[i].v1 ,graph[i].v2 , ' - ',graph[i].lenth, end = '\t')
        if i % columnCount == columnCount - 1: print()
    print()

def Qsort(array, low, high):
    global N1
    if (low < high):
        pivot = low
        i = low
        j = high
 
        while (i < j):
            while array[i].lenth <= array[pivot].lenth and i < high:
                N1+=1
                i += 1
            while array[j].lenth > array[pivot].lenth:
                N1+=1
                j -= 1
 
            if (i < j):
                N1+=3
                array[i], array[j] = array[j], array[i]
                 
        array[pivot], array[j] = array[j], array[pivot]
        Qsort(array, low, j - 1)
        Qsort(array, j + 1, high)
        return array
    else:
        return array

def MinSpanTree(graph, vert):
    global N1
    answ = []
    connectComp = []
    for i in vert:
        connectComp.append([i])
    sortGraph = Qsort(graph, 0, len(origGraph) - 1)
    for i in sortGraph:
        compInd1 = compInd2 = -1
        for j in range(len(connectComp)):
            for k in range(len(connectComp[j])):
                N1 += 1
                if connectComp[j][k] == i.v1: compInd1 = j
                elif connectComp[j][k] == i.v2: compInd2 = j
        if compInd1 != compInd2:
            N1 += 1
            l1 = connectComp[compInd1]
            l2 = connectComp[compInd2]
            connectComp.remove(l1)
            connectComp.remove(l2)
            l1.extend(l2)
            connectComp.insert(0, l1)
            answ.append(i)

    return answ


#origGraph = [Edge('A', 'B', 7), Edge('A', 'C', 8), Edge('B', 'C', 11), Edge('B', 'D', 2), Edge('C', 'D', 6),
#             Edge('C', 'E', 9), Edge('D', 'E', 11), Edge('D', 'F', 9), Edge('E', 'F', 10)]
#vert = ['A','B','C','D','E','F']

origGraph = [Edge('1', '2', 20), Edge('2', '3', 5), Edge('3', '4', 13), Edge('4', '5', 17), Edge('5', '6', 28),
             Edge('6', '1', 23), Edge('1', '7', 1), Edge('2', '7', 4), Edge('3', '7', 9), Edge('4', '7', 16),
             Edge('5', '7', 25), Edge('6', '7', 36)]
vert = ['1','2','3','4','5','6','7']
answ = MinSpanTree(origGraph[:], vert)

print("\nOrig:")
printGraph(origGraph, 3)

print("\nAnswer:")
printGraph(answ, 2)
print("\nN1 = ",N1)
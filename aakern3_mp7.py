def countDown():
    return mylist(10)
def mylist(n):
    if n != 0:
        return [n] + mylist (n-1)
    else:
        return ['Liftoff!']
#print(countDown())


def myLSearch(x, myList):
    for i in range(len(myList)):
        if x == myList[i]:
            return i
    return -1

#print(myLSearch(5, [1,2,3,4,5,6,7]))

def rSearchHelper(x, myList, index):
    if index == len(myList):
        return -1
    if x == myList[index]:
        return index
    return rSearchHelper(x, myList, index+1)
def myRSearch(x, myList):
    return rSearchHelper(x, myList, 0)
#print(myRSearch(3, (1,3,5)))
#print(myRSearch(1, (1,3,5)))
#print(myRSearch(4, (1,3,5)))
#print(myRSearch(6, (5,7,8)))
#print(myRSearch(7, (5,7,8)))
#print(myRSearch(10, (5,7,8,10)))


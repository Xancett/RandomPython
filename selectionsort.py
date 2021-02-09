def SortList(myList):
    for x in range(len(myList)):
        minValue = myList[x]
        print("Index-x: ", x, " value: ", myList[x])
        for y in range(x + 1, len(myList)):
            print("Index-y", y, " value: ", myList[y])
            if (myList[y] < minValue):
                minValue = myList[y]
        myList.remove(minValue)
        myList.insert(x, minValue)

someList = [64, 25, 12, 22, 11]
SortList(someList)
print(someList)
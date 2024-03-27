def main():
    testCases =[
    [1, 1, 1],
    [1, 2, 3],
    [10, 2, -2, -20, 10],
    [3, 1, 2, 4],
    [2, 2, 2],
    [3, 2, 1],
    [2, 2, -4, 1, 1, 2],
    [9, 4, 20, 3, 10, 5],
    [3, 4, 7, -2, 2, 1, 4, 2],
    [1, 2, 1, 2, 1],
    [2, 3, 6, 5, 4, 1, 10],
    [-4, 3, 6, -2, 1, -1, 0, 2, -2, 3, 1],
    [1, -1, 0],
    [0, 1, 1, 1],
    [3, 5, -2, 4, 1, 2, 3]]

    testKValues = [2,3,-10,6,4,3,-3,33,7,3,5,5,0,3,3]
    expectedResults = [2,2,3,2,2,2,1,2,6,4,3,3,3,2,5]
    numTestCases = len(testCases)
    numPassed = 0
    for i in range(numTestCases):
        if subarraySum(testCases[i], testKValues[i]) == expectedResults[i]:

            numPassed += 1
        else:
            print("Failed")
    
    print("{}/{}".format(numPassed, numTestCases))

if __name__ == "__main__":
    main()

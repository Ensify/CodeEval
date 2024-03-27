
def main():
    testCases = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16]
    expectedResults = [1, 2, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108, 162, 243,324]

    numTestCases = len(testCases)
    numPassed = 0
    for i in range(numTestCases):
        if helper(testCases[i]) == expectedResults[i]:
            numPassed += 1

    print("{}/{}".format(numPassed, numTestCases))

if __name__ == "__main__":
    main()


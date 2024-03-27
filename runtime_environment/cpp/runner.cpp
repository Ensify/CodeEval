
#include <bits/stdc++.h>
using namespace std;

int pivotInteger(int n);
int main() {
    vector<int> testCases = {
        8,1,4,21,22,36
    };
    vector<int> expectedResults = {
        6,1,-1,-1,-1,-1
    };
    int numTestCases = testCases.size();
    int numPassed = 0;
    for (int i = 0; i < numTestCases; i++) {
        cout << "Test case " << i + 1 << ": ";
        if (pivotInteger(testCases[i])==expectedResults[i]) {
            cout << "Passed" << endl;
            numPassed++;
        } else {
            cout << "Failed" <<endl;
        }
    }
    if (numPassed == numTestCases) {
        cout << "All test cases passed! Problem solved." << endl;
    } else {
        cout << "Number of test cases passed: " << numPassed << "/" << numTestCases << endl;
    }
    return 0;
}
int pivotInteger(int n) {
    return 0;
}

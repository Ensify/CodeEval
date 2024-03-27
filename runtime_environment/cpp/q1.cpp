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
        if (pivotInteger(testCases[i])==expectedResults[i]) {
            numPassed++;
        }
    }

    cout << numPassed << "/" << numTestCases << endl;
    
    return 0;
}

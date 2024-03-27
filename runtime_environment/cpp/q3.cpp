#include <bits/stdc++.h>
using namespace std;


int helper(int n);

int main() {
    vector<int> testCases = {
        2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
    };
    vector<int> expectedResults = {
        1,2,4,6,9,12,18,27,36,54,81,108,162,243,324
    };
    int numTestCases = testCases.size();
    int numPassed = 0;
    for (int i = 0; i < numTestCases; i++) {
        if (helper(testCases[i])==expectedResults[i]) {
            numPassed++;
        } 
    }

    cout << numPassed << "/" << numTestCases << endl;

    return 0;
}

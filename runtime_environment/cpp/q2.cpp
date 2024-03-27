#include <bits/stdc++.h>
using namespace std;
int minimumParentheses(string pattern);
int main() {
    vector<string> testCases = {
        ")((()","((","(((((","))(","()",")(((((","(((()","((((((",")())","((",
        "(","(()((()(",")()())","(()",")()()",")()((()",
        ")()))()",
        "(()",")(())",")((","(","((()()((","()(",")","((())))","(","))","((",
        "))))",")()((","()()","()(","(()()","()(())(",")",")())))((",")()("
    };
    vector<int> expectedResults = {
        3,2,5 ,3,0,6,3,6,2,
        2,1,4,2,1,1,
        3,3,1,1,3,1,4,1,1,1,1,2,2,4,3,0,1,1,1,1,6,2
    };
    int numTestCases = testCases.size();
    int numPassed = 0;
    for (int i = 0; i < numTestCases; i++) {
        if (minimumParentheses(testCases[i])==expectedResults[i]) {
            numPassed++;
        } 
    }
    cout << numPassed << "/" << numTestCases << endl;
    return 0;
}


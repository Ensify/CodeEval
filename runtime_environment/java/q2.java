import java.util.*;

public class Runner {

    public static void main(String[] args) {
        List<String> testCases = Arrays.asList(
            ")((()","((","(((((","))(","()",")(((((","(((()","((((((",")())","((",
        "(","(()((()(",")()())","(()",")()()",")()((()",
        ")()))()",
        "(()",")(())",")((","(","((()()((","()(",")","((())))","(","))","((",
        "))))",")()((","()()","()(","(()()","()(())(",")",")())))((",")()("
        );

        List<Integer> expectedResults = Arrays.asList(
            3,2,5 ,3,0,6,3,6,2,
        2,1,4,2,1,1,
        3,3,1,1,3,1,4,1,1,1,1,2,2,4,3,0,1,1,1,1,6,2
        );

        int numTestCases = testCases.size();
        int numPassed = 0;

        for (int i = 0; i < numTestCases; i++) {
            System.out.print("Test case " + (i + 1) + ": ");
            if (minimumParentheses(testCases.get(i)) == expectedResults.get(i)) {
                System.out.println("Passed");
                numPassed++;
            } else {
                System.out.println("Failed");
            }
        }

        if (numPassed == numTestCases) {
            System.out.println("All test cases passed! Problem solved.");
        } else {
            System.out.println("Number of test cases passed: " + numPassed + "/" + numTestCases);
        }
    }


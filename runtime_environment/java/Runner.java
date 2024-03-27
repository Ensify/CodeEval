import java.util.ArrayList;
import java.util.List;

public class Runner {
    public static void main(String[] args) {
        List<Integer> testCases = List.of(8,1,4,21,22,36);
        List<Integer> expectedResults = List.of(6,1,-1,-1,-1,-1);
        int numTestCases = testCases.size();
        int numPassed = 0;
        for (int i = 0; i < numTestCases; i++) {
            System.out.print("Test case " + (i + 1) + ": ");
            if (pivotInteger(testCases.get(i)) == expectedResults.get(i)) {
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

public static int pivotInteger(int n) {
        return 0;
    }}
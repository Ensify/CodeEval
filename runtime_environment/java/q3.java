import java.util.ArrayList;

public class Runner {

    public static void main(String[] args) {
        ArrayList<Integer> testCases = new ArrayList<Integer>();
        ArrayList<Integer> expectedResults = new ArrayList<Integer>();

        testCases.add(2);
        expectedResults.add(1);
        testCases.add(3);
        expectedResults.add(2);
        testCases.add(4);
        expectedResults.add(4);
        testCases.add(5);
        expectedResults.add(6);
        testCases.add(6);
        expectedResults.add(9);
        testCases.add(7);
        expectedResults.add(12);
        testCases.add(8);
        expectedResults.add(18);
        testCases.add(9);
        expectedResults.add(27);
        testCases.add(10);
        expectedResults.add(36);
        testCases.add(11);
        expectedResults.add(54);
        testCases.add(12);
        expectedResults.add(81);
        testCases.add(13);
        expectedResults.add(108);
        testCases.add(14);
        expectedResults.add(162);
        testCases.add(15);
        expectedResults.add(243);
        testCases.add(16);
        expectedResults.add(324);

        int numTestCases = testCases.size();
        int numPassed = 0;
        for (int i = 0; i < numTestCases; i++) {
            System.out.print("Test case " + (i + 1) + ": ");
            if (helper(testCases.get(i)) == expectedResults.get(i)) {
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

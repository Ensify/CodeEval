import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<Integer> testCases = List.of(8,1,4,21,22,36);
        List<Integer> expectedResults = List.of(6,1,-1,-1,-1,-1);
        int numTestCases = testCases.size();
        int numPassed = 0;
        for (int i = 0; i < numTestCases; i++) {
            if (pivotInteger(testCases.get(i)) == expectedResults.get(i)) {
                numPassed++;
        }
        System.out.println(numPassed + "/" + numTestCases);
        
    }

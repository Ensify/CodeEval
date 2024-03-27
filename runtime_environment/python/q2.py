

def main():
    test_cases = [
        ")((()","((","(((((","))(","()",")(((((","(((()","((((((",")())","((",
        "(","(()((()(",")()())","(()",")()()",")()((()",
        ")()))()",
        "(()",")(())",")((","(","((()()((","()(",")","((())))","(","))","((",
        "))))",")()((","()()","()(","(()()","()(())(",")",")())))((",")()("
    ]
    expected_results = [
        3,2,5 ,3,0,6,3,6,2,
        2,1,4,2,1,1,
        3,3,1,1,3,1,4,1,1,1,1,2,2,4,3,0,1,1,1,1,6,2
    ]
    num_test_cases = len(test_cases)
    num_passed = 0
    for i in range(num_test_cases):
        if minimum_parentheses(test_cases[i]) == expected_results[i]:
            num_passed += 1

    print(f"{num_passed}/{num_test_cases}")

if __name__ == "__main__":
    main()

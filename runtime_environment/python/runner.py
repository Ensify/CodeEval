def pivot_integer(*a):
    return "ok"

if __name__ == "__main__":
    test_cases = [8,1,4,21,22,36]
    expected_results = [6,1,-1,-1,-1,-1]
    num_test_cases = len(test_cases)
    num_passed = 0
    for i in range(num_test_cases):
        if pivot_integer(test_cases[i]) == expected_results[i]:
            num_passed += 1

    print(f"{num_passed}/{num_test_cases}")

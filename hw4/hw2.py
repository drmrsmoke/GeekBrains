test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"{[test_list[n] for n in range(1, len(test_list)) if test_list[n - 1] < test_list[n]]}")


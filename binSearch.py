def binSearch(n, target):
    left = 0
    right = len(n) - 1

    while left <= right:
        mid = left + (right - left) // 2  # operator precedence
        if n[mid] == target:
            return mid
        elif n[mid] > target:
            right = mid - 1
        elif n[mid] < target:
            left = mid + 1


def binSearchTest(binSearch):
    n = [1, 5, 10, 15, 20]
    m = [5, 6, 7, 8, 9, 10]

    if binSearch(n, 1) != 0:
        print("the test failed")
    else:
        print(
            f"test successful!\nVaraibles: array: {n}, target value: 1\nResult: {binSearch(n, 1)}\n"
        )

    if binSearch(m, 8) != 3:
        print("the test failed")
    else:
        print(
            f"test successful!\nVaraibles: array: {m}, target value: 8\nResult: {binSearch(m, 8)}"
        )


print("test for binary search implementation")
binSearchTest(binSearch)

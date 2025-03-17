class Solution:
    @staticmethod
    def reverseString(s: list[str]) -> None:
        # Do not return anything, modify s in-place instead.
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1


s: list[str] = ["h", "a", "l", "l", "o"]

print(f"before test {s}")
Solution.reverseString(s)
print(f"after test {s}")

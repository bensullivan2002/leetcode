class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        results: dict[int, int] = {}
        window = nums[:l]
        window_sum = sum(window)
        results[0] = window_sum
        print(max(results, key=results.__getitem__))
        return 0

def main():
    test_solution = Solution()
    test_solution.minimumSumSubarray([3, -2, 1, 4], 2, 3)

if __name__ == "__main__":
    main()

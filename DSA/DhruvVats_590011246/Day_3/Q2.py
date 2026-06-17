class Solution:
    def countFreq(self, arr, target):
        def first_occurrence():
            low, high = 0, len(arr) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == target:
                    ans = mid
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        def last_occurrence():
            low, high = 0, len(arr) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == target:
                    ans = mid
                    low = mid + 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        first = first_occurrence()

        if first == -1:
            return 0

        last = last_occurrence()

        return last - first + 1
# Day 3 solution
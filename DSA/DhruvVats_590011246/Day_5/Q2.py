class Solution:
    def checkEqualArrays(self, a, b):
        if len(a) != len(b):
            return False

        freq = {}

        for num in a:
            freq[num] = freq.get(num, 0) + 1

        for num in b:
            if num not in freq:
                return False

            freq[num] -= 1

            if freq[num] == 0:
                del freq[num]

        return len(freq) == 0
#Day 5 solution
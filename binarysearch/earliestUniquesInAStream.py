from collections import Counter

class EarliestUnique:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def add(self, num: int) -> None:
        self.nums.append(num)
        
    def earliestUnique(self) -> int:
        count = Counter(self.nums)
        for i in set(self.nums):
            if count[i] == 1:
                return i
        return -1

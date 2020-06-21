import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, nums: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, nums)

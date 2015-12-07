"""
275. H-Index II
Follow up for H-Index: What if the citations array is sorted in ascending order?
Could you optimize your algorithm?
"""
# O(logn)
# O(1)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        lower, upper = 0, len(citations) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            if citations[mid] > len(citations) - mid:
                upper = mid
            else:
                lower = mid + 1
        if citations[lower] >= len(citations) - lower:
            return len(citations) - lower
        return len(citations) - lower - 1

if __name__ == "__main__":
    print(Solution().hIndex([1, 2, 2, 3, 4, 4, 5, 7]))

"""
163. Missing Ranges
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""
# O(n)
# O(1)
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        start, end, res = lower, upper, []
        for i in range(len(nums)):
            if nums[i] < lower:
                continue
            if nums[i] > upper:
                if start == upper:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(upper))
                break
            if nums[i] == start:
                start += 1
            else:
                end = nums[i] - 1
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = nums[i] + 1
        else:
            if start == upper:
                res.append(str(start))
            elif start < upper:
                res.append(str(start) + "->" + str(upper))
        return res

if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75]
    lower, upper = 0, 99
    print(Solution().findMissingRanges(nums, lower, upper))

"""
135. Candy
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
# O(n)
# O(n)
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        res_left, res_right = [1], [1]
        i = 1
        while i < len(ratings):
            if ratings[i] > ratings[i - 1]:
                res_left.append(res_left[-1] + 1)
            else:
                res_left.append(1)
            i += 1
        j = len(ratings) - 2
        while j >= 0:
            if ratings[j] > ratings[j + 1]:
                res_right.append(res_right[-1] + 1)
            else:
                res_right.append(1)
            j -= 1
        res_right.reverse()
        res = 0
        for i in range(len(res_left)):
            res += max(res_left[i], res_right[i])
        return res

if __name__ == "__main__":
    print(Solution().candy([3, 5, 4, 1, 7, 7, 8, 1]))

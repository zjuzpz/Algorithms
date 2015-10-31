"""
299. Bulls and Cows
You are playing the following Bulls and Cows game with your friend: You write a 4-digit secret number and ask your friend to guess it, each time your friend guesses a number, you give a hint, the hint tells your friend how many digits are in the correct positions (called "bulls") and how many digits are in the wrong positions (called "cows"), your friend will use those hints to find out the secret number.

For example:

Secret number:  1807
Friend's guess: 7810
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
"""
# O(n)
# O(1)
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B, lookup = 0, 0, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] not in lookup:
                    lookup[secret[i]] = 1
                elif lookup[secret[i]] >= 0:
                    lookup[secret[i]] += 1
                else:
                    B += 1
                    lookup[secret[i]] += 1
                if guess[i] not in lookup:
                    lookup[guess[i]] = -1
                elif lookup[guess[i]] <= 0:
                    lookup[guess[i]] -= 1
                else:
                    B += 1
                    lookup[guess[i]] -= 1
        return str(A) + "A" + str(B) + "B"

if __name__ == "__main__":
    print(Solution().getHint("1245", "2548"))

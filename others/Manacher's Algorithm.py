#Manacher's Algorithm
# O(n)
# O(n)

def longestPalindrome(s):
    if not s:
        return ""
    s_p = preProcess(s)
    center, right, max_index, res = 0, 0, 0, [0 for i in s_p]
    for i in range(1, len(s_p) - 1):
        if i < right:
            i_mirror = 2 * center - i
            res[i] = min(res[i_mirror], right - i)
        while s_p[i - res[i] - 1] == s_p[i + res[i] + 1]:
            res[i] += 1
        if res[i] + i > right:
            center = i
            right = res[i] + i
        if res[i] > res[max_index]:
            max_index = i
    index = (max_index - 1 - res[max_index]) // 2
    return s[index: index + res[max_index]]

def preProcess(s):
    res = "^#"
    for i in s:
        res += i + "#"
    return res + "$"

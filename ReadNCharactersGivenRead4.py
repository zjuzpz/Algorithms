"""
157. Read N Characters Given Read4
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.
"""

def read4(buf):
    global file
    i = 0
    while i < len(file) and i < 4:
        buf[i] = file[i]
        i += 1
    if len(file) > 4:
        file = file[4:]
    else:
        file = ""
    return i
    
# O(n)
# O(1)
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        times, reminder, res, buf_4 = n // 4, n % 4, 0, ["" for i in range(4)]
        for i in range(times):
            tem = read4(buf_4)
            res += tem
            buf[i * 4 : i * 4 + tem] = buf_4[:]
            if tem < 4:
                return res
        tem = read4(buf_4)
        if tem <= reminder:
            buf[times * 4 : times * 4 + tem] = buf_4[0 : tem]
            return res + tem
        buf[times * 4 : n] = buf_4[0 : reminder]
        return n

if __name__ == "__main__":
    global file
    buf = ['' for i in range(10)]
    file = "a"
    length = Solution().read(buf, 4)
    print(length, buf[0 : length])
    file = "abcdef"
    length = Solution().read(buf, 10)
    print(length, buf[0 : length])
    

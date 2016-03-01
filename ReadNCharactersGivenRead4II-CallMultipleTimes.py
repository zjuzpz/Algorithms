"""
158. Read N Characters Given Read4 II - Call multiple times
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""
# O(n)
# O(1)
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

class Solution(object):
    def __init__(self):
        self.buf = ["" for i in range(4)]
        self.cur = 0
        self.buf_size = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        eof, readBytes = False, 0
        while not eof and readBytes < n:
            if self.buf_size > 0:
                size = self.buf_size
            else:
                size = read4(self.buf)
            if self.buf_size == 0 and size < 4:
                eof = True
            bytes = min(size, n - readBytes)
            for i in range(bytes):
                buf[readBytes + i] = self.buf[self.cur + i]
            self.buf_size = size - bytes
            self.cur = (self.cur + bytes) % 4
            readBytes += bytes
        return readBytes

class Solution2(object):
    def __init__(self):
        self.buf = ["" for i in range(4)]
        self.start = 0
        self.end = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.start < self.end:
                buf[i] = self.buf[self.start]
                self.start, i = self.start + 1, i + 1
            else:
                self.end = read4(self.buf)
                if self.end:
                    self.start = 0
                else:
                    break
        return i
            

if __name__ == "__main__":
    global file
    sol = Solution2()
    buf = ['' for _ in range(100)]
    file = "1234567"
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 1)])

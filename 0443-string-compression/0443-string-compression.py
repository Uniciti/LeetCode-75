class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0
        read = 0

        while read < n:
            current = chars[read]
            count = 0

            while read < n and chars[read] == current:
                count += 1
                read += 1

            chars[write] = current
            write += 1

            if count > 1:
                for v in str(count):
                    chars[write] = v
                    write += 1
                    
        return write
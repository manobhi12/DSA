class Solution:
    def compress(self, chars):

        n = len(chars)

        i = 0
        write = 0

        while i < n:

            current = chars[i]
            count = 0


            while i < n and chars[i] == current:
                i += 1
                count += 1

       
            chars[write] = current
            write += 1

         
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
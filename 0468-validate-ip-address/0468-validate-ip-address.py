class Solution:

    def validIPAddress(self, queryIP: str) -> str:

   
        if queryIP.count('.') == 3:

            parts = queryIP.split('.')

            for part in parts:

 
                if (not part or
                    (len(part) > 1 and part[0] == '0')):
                    return "Neither"

  
                if not part.isdigit():
                    return "Neither"

         
                if not (0 <= int(part) <= 255):
                    return "Neither"

            return "IPv4"


        if queryIP.count(':') == 7:

            hex_digits = "0123456789abcdefABCDEF"

            parts = queryIP.split(':')

            for part in parts:

        
                if not (1 <= len(part) <= 4):
                    return "Neither"

         
                for ch in part:
                    if ch not in hex_digits:
                        return "Neither"

            return "IPv6"

        return "Neither"
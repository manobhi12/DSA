class Solution:
    def deserialize(self, s: str) -> NestedInteger:


        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []

        num = ""
        negative = False

        for ch in s:

       
            if ch == '[':
                stack.append(NestedInteger())

        
            elif ch == '-':
                num += ch

     
            elif ch.isdigit():
                num += ch

  
            elif ch == ',' or ch == ']':

           
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""

            
                if ch == ']' and len(stack) > 1:
                    nested = stack.pop()
                    stack[-1].add(nested)

        return stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        # init stack
        stack = []
        # store bracket into a dict
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        # iterate through s
        for bracket in s:
            # if open -> ([{
            if bracket in brackets:
                stack.append(bracket)
            # else
            else:
                # if close vs top of stack
                if not stack or brackets[stack[-1]] != bracket:
                    return False
                
                stack.pop()

        return not stack
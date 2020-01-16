class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == ')' or i == '[' or i == ']' or i == '{' or i == '}':
                if i == ')':
                    if len(stack) != 0 and stack[len(stack)-1] == '(':
                        stack.pop()
                    else:
                        return False

                if i == ']':
                    if len(stack) != 0 and stack[len(stack)-1] == '[':
                        stack.pop()
                    else:
                        return False

                if i == '}':
                    if len(stack) != 0 and stack[len(stack)-1] == '{':
                        stack.pop()
                    else:
                        return False

                if i == '(' or i == '[' or i == '{':
                    stack.append(i)

        return len(stack) == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid(']'))
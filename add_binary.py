class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        total = ''
        num1 = int(a)
        num2 = int(b)
        n1 = 0
        n2 = 0
        if (num1 == 0) and (num2 == 0):
            return str(0)
        while num1 != 0 or num2 != 0:
            n1 = num1 % 10
            n2 = num2 % 10
            print(n1, ' ',n2)
            if carry == 1:
                if n1 + n2 == 0:
                    total = total + '1'
                    carry = 0
                if n1 + n2 == 1:
                    total = total + '0'
                if n1 + n2 == 2:
                    total = total + '1'
            else:
                if n1 + n2 == 2:
                    total = total + '0'
                    carry = 1
                else:
                    total = total + str(n1 + n2)
            print(total)
            num1 = num1 // 10
            num2 = num2 // 10
            print(num1, ' ',num2)
        if num1 != 0:
            total = total + num1
        if num2 != 0:
            total = total + num2
        if carry == 1:
            total = total + '1'
        return total[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary('0', '0'))
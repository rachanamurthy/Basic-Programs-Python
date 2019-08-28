'''
Check if a provided number is a palindrome
'''

def palindrome(x):
  if x < 0:
    return False
  else:
    if (check_palindrome(x,0) == x):
      return True
    else:
      return False

def check_palindrome(n,rev):
  if n == 0:
    return rev
  else:
    i = n % 10
    rev = rev * 10 + i
    n = n // 10
    return(check_palindrome(n,rev))

print(palindrome(10))


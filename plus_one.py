# This solution is faster than 99.64% of the solutions

def plusOne(digits):
  for i in range(len(digits) - 1,-1,-1):
    print(digits[i])
    digits[i] = digits[i] + 1
    if digits[i] > 9:
      digits[i] = 0
      if (digits[i] == 0) and (i == 0):
        digits.insert(0,1)
    else:
      break
  print(digits)

plusOne([9,9])
        
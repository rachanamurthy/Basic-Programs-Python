'''
This program prints the even numbers
'''

def print_even():
  for element in range(2,100):
    if (element % 2 == 0):
      print(element)

if __name__ == '__main__':
  print_even()
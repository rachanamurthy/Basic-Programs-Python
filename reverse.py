'''
Print the reverse of a number
'''
def reverse(x):
    if (x < 0):
        x = abs(x)
        return(-1 * reverse_recursive(x,0))
    else:
        return(reverse_recursive(x,0))

def reverse_recursive(n,rev):
    if n == 0:
        return int(rev)
    else:
        i = n % 10
        rev = rev * 10 + i
        n = n // 10
        return(reverse_recursive(n,rev)) 

if __name__ == '__main__':
    print(reverse(123))    
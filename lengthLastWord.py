# Runtime: 20 ms, faster than 98.28% of Python3 online submissions for Length of Last Word.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Length of Last Word.

def lengthOfLastWord(s):
    words = s.split(' ')
    print(words)
    if len(words) == 0:
        return 0
    elif len(words) == 1:
        return len(words[0])
    elif len(words[-1]) == 0:
        count = -2
        while (-1 * count) < len(words) and len(words[count]) == 0:
            print(count)
            count = count - 1
        return len(words[count])
    else:
        return len(words[-1])


if __name__ == '__main__':
    print(lengthOfLastWord('  '))
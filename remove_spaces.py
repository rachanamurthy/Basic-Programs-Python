def replace(str1):
    length = len(str1)
    letters = list(str1)
    for i in range(length-1, -1, -1):
        if str1[i] == ' ':
            letters[i] = '&'
        else:
            count = i
            break
    letters_new = letters[:]

    for i in range(count, -1, -1):
        if letters_new[i] == ' ':
            letters_new[i] = '%'
            for j in range(i+3, length):
                letters_new[j] = letters[j-2]
            letters_new[i + 1] = '2'
            letters_new[i + 2] = '0'
            letters = letters_new[:]
    return ''.join(letters_new)


def main():
    sentence = 'oh my god    '
    print('Replaced string', replace(sentence))


if __name__ == '__main__':
    main()
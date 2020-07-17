def check_replace(str1, str2):
    count = {}
    for i in str1:
        if count.__contains__(i):
            count[i] = count[i] + 1
        else:
            count[i] = 1
    oneLetterIsNotPresent = False
    for i in str2:
        if count.__contains__(i):
            count[i] = count[i] - 1
            if count[i] == 0:
                del count[i]
        else:
            if oneLetterIsNotPresent:
                return False
            oneLetterIsNotPresent = True

    if len(count.keys()) == 1 and oneLetterIsNotPresent:
        return True
    else:
        return False


def check(str1, str2):
    count = {}
    for i in str1:
        if count.__contains__(i):
            count[i] = count[i] + 1
        else:
            count[i] = 1

    oneLetterNo = False

    for i in str2:
        if not count.__contains__(i):
            if oneLetterNo:
                return False
            else:
                oneLetterNo = True
        else:
            count[i] = count[i] - 1
            if count[i] == 0:
                del count[i]

    if len(count.keys()) == 0 and oneLetterNo:
        return True
    else:
        return False


def one_way(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 < len2:
        return check(str1, str2)
    elif len2 < len1:
        return check(str2, str1)
    else:
        return check_replace(str1, str2)


def main():
    str1 = 'ac'
    str2 = 'bc'
    if one_way(str1, str2):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
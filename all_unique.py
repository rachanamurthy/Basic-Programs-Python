def check_unique(str):
    letters = {}
    for char in str:
        if letters.__contains__(char):
            return False
        letters[char] = True
    return True

def main():
    if check_unique:
        print('Yes Unique')
    else:
        print('Not unique')


if __name__ == '__main__':
    main()
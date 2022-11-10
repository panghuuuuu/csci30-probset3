#!/usr/bin/env python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# note: if you're having errors with the type hints, you can just remove them
def martian_sort(wordlist: list[str], order: list[int]) -> list[str]:
    # TO-DO

# DON'T TOUCH the code below
if __name__ == '__main__':
    order = list(map(int, input().split()))
    wordlist = input().split()
    sorted_words = ' '.join(martian_sort(wordlist, order))
    print(sorted_words)
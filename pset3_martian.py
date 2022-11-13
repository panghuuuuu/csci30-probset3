#!/usr/bin/env python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def martian_sort(wordlist, order):
    final_sort = []
    wordlist = [wordlist]
    for i in range(len(order)):
        x = len(wordlist)
        for j in range(x):
            current_word_list = wordlist[j]
            current_order = order[i]
            if (len(current_word_list) == 1):
                wordlist.append(current_word_list)
            else:
                letters = list(set([k[order[i]] for k in current_word_list]))
                if (len(letters) <= 1):
                    wordlist.append(current_word_list)
                else:
                    letters = sort_set(letters)
                    pre_list = [[y for y in current_word_list if y[current_order] == x] for x in letters]
                    for k in pre_list:
                        wordlist.append(k)
        wordlist = wordlist[x:]
    for l in (wordlist):
        final_sort +=  l
    return final_sort

def sort_set(bucket_list):
    if len(bucket_list) < 2:
        return bucket_list 
    else:
        pivot = bucket_list[0]
        lower = [i for i in bucket_list[1:] if i <= pivot] 
        upper = [i for i in bucket_list[1:] if i > pivot]
        return sort_set(lower) + [pivot] + sort_set(upper)

if __name__ == '__main__':
    order = list(map(int, input().split()))
    wordlist = input().split()
    sorted_words = ' '.join(martian_sort(wordlist, order))
    print(sorted_words)
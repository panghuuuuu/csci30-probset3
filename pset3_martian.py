#!/usr/bin/env python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# note: if you're having errors with the type hints, you can just remove them
def martian_sort(wordlist: list[str], order: list[int]) -> list[str]:
    sorted_string = []
    sorted_string = sort_in_buckets(bucket_letters(wordlist, order[0]), 1, order)
    final_string = []
    for i in range(len(sorted_string)):
        for j in range(len(sorted_string[i])):
            final_string.append(sorted_string[i][j])
    return final_string

def sort_set(bucket_list: list[str]) -> list[str]:
    alphabet_order = list(alphabet)
    temp = ''
    for i in range(len(bucket_list)):
        for j in range(i + 1, len(bucket_list)):
            if alphabet_order.index(bucket_list[i]) > alphabet_order.index(bucket_list[j]):
                temp = bucket_list[i]  
                bucket_list[i] = bucket_list[j]
                bucket_list[j] = temp
    return bucket_list

def bucket_letters(wordlist: list[str], charac_index: int) -> list[str]:
    letters = list(set([i[charac_index] for i in wordlist]))
    letters = sort_set(letters)
    d = {j:j[charac_index] for j in wordlist}
    bucket = []
    for i in range(len(letters)):
        bucket.append([])
    for k, v in d.items():
        bucket[letters.index(v)].append(k)
    return bucket

def sort_in_buckets(my_list: list[list], index: int, order: list[int]) -> list[str]:
    if (index == len(order)):
        return my_list
    else:
        x = len(my_list)
        for i in range(x):
            new = my_list[0]
            bucketed = bucket_letters(new, order[index])
            for j in range(len(bucketed)):
                my_list.append(bucketed[j])
            my_list.pop(0)
        sort_in_buckets(my_list, index+1, order)
    return my_list
    
# DON'T TOUCH the code below
if __name__ == '__main__':
    order = list(map(int, input().split()))
    wordlist = input().split()
    sorted_words = ' '.join(martian_sort(wordlist, order))
    print(sorted_words)
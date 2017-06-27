def get_words():
    '''Get the words to be checked from user input'''

    word1 = input("Enter A Word: ")
    word2 = input("Enter A Word: ")

    return word1, word2

def check_words(word1, word2):
    '''Check if two words are anagrams of one-another'''

    if len(word1) != len(word2):
        return False

    dict1 = {}
    dict2 = {}

    for i in word1:
        if i not in dict1:
            dict1[i] = 0
        else:
            dict1[i] += 1

    for i in word2:
        if i not in dict2:
            dict2[i] = 0
        else:
            dict2[i] += 1

    if dict1 == dict2:
        return True
    else:
        return False

def main():
    print('This script checks if two words are anagrams of each other.')
    word1, word2 = get_words()
    print(check_words(word1, word2))

main()

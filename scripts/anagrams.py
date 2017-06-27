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

    for i in word1:             # Iterate over the letters of word1
        if i not in dict1:      # If we haven't seen the letter before 
            dict1[i] = 1        # Make an entry and initialize its count to 1 
        else:
            dict1[i] += 1       # Else increment the count

    for i in word2:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] += 1

    if dict1 == dict2:          # If the words have the same number of each letter
        return True             # They are anagrams
    else: 
        return False            # Else they are not

def main():
    print('This script checks if two words are anagrams of each other.')
    word1, word2 = get_words()
    print(check_words(word1, word2))

main()

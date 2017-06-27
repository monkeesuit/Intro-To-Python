def get_word():
    '''Get the word to be checked from user input'''

    word = input("Enter A Word: ")
    return word

def check_word(word):
    '''Check if the word is a palindrome'''
    
     # We want to split the word in half and ignore the middle letter if word has an odd length
     # And iterate over the most outside letters of word moving towards the center  
    length = len(word)
    for i in range(length//2):              
        left = i
        right = -(i+1)
        if word[left] != word[right]:       # If those letter are not the same then the word is not a palindrome
            return False
        return True

def main():
    print("This script checks if a word is a Palindrome.")
    word = get_word()
    print(check_word(word))

main()

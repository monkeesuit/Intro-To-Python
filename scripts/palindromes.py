def get_word():
    '''Get the word to be checked from user input'''

    word = input("Enter A Word: ")
    return word

def check_word(word):
    '''Check if the word is a palindrome'''
    
    length = len(word)
    for i in range(length//2):
        left = i
        right = -(i+1)
        if word[left] != word[right]:
            return False
        return True

def main():
    print("This script checks if a word is a Palindrome.")
    word = get_word()
    print(check_word(word))

main()

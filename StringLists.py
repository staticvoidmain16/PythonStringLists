user_word = input("Please enter a word: ")

reverse = user_word[::-1]

if user_word == reverse:
    print("%s is a palindrome" % user_word)
else:
    print("%s is not a palindrome" % user_word)
    

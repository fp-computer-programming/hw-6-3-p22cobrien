# Author: CMOB 11/15/2021

word1 = list(input("Please enter a word. "))
word2 = list(input("Please enter another word. "))

word1.sort()
word2.sort()

if word1 == word2:
    print("The two words are an anogram.")
else:
    print("The two words aren't an anogram.")

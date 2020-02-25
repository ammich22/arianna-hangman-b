from __future__ import print_function

word = "earring"
lives = 6
spaces = [('_') * len(word)]

def main():
    initialize()
    getLetter()
    #check()
    
def initialize():
    print(''.join(spaces))
    
def getLetter():
    firstLetter = raw_input("Guess a letter: ")
    lives = 6
    if firstLetter in word:
        if firstLetter == 'e':
            print ('e _ _ _ _ _ _ _')
        if firstLetter == 'a':
            print ('_ a _ _ _ _ _ _')
        if firstLetter == 'r':
            print ('_ _ r r _ _ _ _')
        if firstLetter == 'i':
            print ('_ _ _ _ i _ _ _')
        if firstLetter == 'n':
            print ('_ _ _ _ _ _ n _')
        if firstLetter == 'g':
            print ('_ _ _ _ _ _ _ g')
    else:
        print('_ _ _ _ _ _ _    Your letter is not in the word. You now have', lives - 1, 'lives.')
        
def win():
    if ('_') in spaces:
        print()

main()
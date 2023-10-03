import os

words = []

def load_words(path):
    file = open(path, 'r')
    global words
    words *= 0

    for word in file:
        words.append(word[:-1])

    file.close()


def eliminate_words(i, char, word):
    to_rem = []

    if char == '=':
        for w in words:
            if w[i] != word[i]:
                to_rem.append(w)
    elif char == '-':
        if word.count(word[i]) < 2:
            for w in words:
                if word[i] in w:
                    to_rem.append(w)
        else:
            for w in words:
                if w.count(word[i]) > 1:
                    to_rem.append(w)
    else:
        for w in words:
            if word[i] not in w or word[i] == w[i]:
                to_rem.append(w)
    
    for w in to_rem:
        words.remove(w)

def main():
    path = "words" #input("Input filepath for wordbank: ")

    
    try_again = "y"

    while try_again == "y":
        load_words(path)
        os.system("cls" if os.name == "nt" else "clear")
        guesses = 0
        num_correct = 0
        
        while guesses < 6 and num_correct < 5:
            next_word = words[0]

            print("NEXT GUESS:", next_word)

            result = input("INPUT RESULT: = IS GREEN, + IS YELLOW, - IS GRAY: ")

            for i,char in enumerate(result):
                eliminate_words(i, char, next_word)

            guesses += 1

            num_correct = result.count("=")
        
        if num_correct == 5:
            try_again = input("CONGRATS! YOU WIN! PLAY AGAIN? (Y/N): ").lower()
        else:
            try_again = input("BAD LUCK, TRY AGAIN? (Y/N): ").lower()
    
    print("----- THANKS FOR PLAYING! -----")

if __name__=="__main__":
    main()
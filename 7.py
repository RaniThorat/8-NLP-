# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:58:38 2023

@author: Admin
"""

def generateEncrypted(plainText):
    matrix = [[' ' for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            matrix[i][j] = ' '

    rounds = int(input("Enter the number of rounds: "))
    round = 1

    while round <= rounds:
        print("For Round", round)
        print("PlainText is:", plainText)
        length = len(plainText)
        index = 0
        isComplete = False

        for i in range(5):
            for j in range(5):
                if index < length and plainText[index] == ' ':
                    index += 1
                if index < length:
                    matrix[i][j] = plainText[index]
                    index += 1
                    if index == length:
                        isComplete = True
                        break
            if isComplete:
                break

        print("Printing Created Matrix")
        for i in range(5):
            for j in range(5):
                print(matrix[i][j], end=' ')
            print()

        input_choices = input("Enter the choices for columns (5 choices 0-4, separated by spaces): ").split()

        if len(input_choices) != 5:
            print("Please provide exactly five choices.")
        else:
            input_choices = list(map(int, input_choices))

            encryptedText = ""
            for it in range(5):
                j = input_choices[it]
                str = ""
                for i in range(5):
                    if matrix[i][j] != ' ':
                        str += matrix[i][j]
                encryptedText += str

            print("After Round", round, "generated Encrypted Text is:", encryptedText)
            plainText = encryptedText
            round += 1

def main():
    plainText = "information security"
    print("Plain Text is:", plainText)
    generateEncrypted(plainText)

if __name__ == "__main__":
    main()
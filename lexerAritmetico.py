import os
import sys
import lexerlib

if __name__ == '__main__':

    #check if argument is passed
    if len(sys.argv) < 2:
        print("No file name passed")
        exit(0)
    
    #read argument
    fileName = sys.argv[1]

    #check if file exists
    if not os.path.isfile(fileName):
        print("File not found")
        exit(0)
    
    #read file
    content = lexerlib.readFile(fileName)

    #split content by lines
    lines = content.split("\N{LF}")

    #will store the identified and labeled elements
    elements = []

    #variables used to identify the state
    operand = False
    asignation = False
    comment = False
    variable = False
    number = False
    bracket = False

    #iterate through lines
    for line in lines:
        #split line by spaces
        words = line.split(" ")
        for word in words:
            #create case based on firs element of word
            if lexerlib.isLetter(word[0]):
                #check if word is a variable
                1+1
            elif lexerlib.isDigit(word[0]):
                #check if word is a number
                1+1
            elif lexerlib.isBracket(word[0]):
                #check if word is a bracket
                1+1
            elif lexerlib.isComment(word):
                #check if word is a comment
                1+1
            elif lexerlib.isOperand(word[0]):
                #check if word is an operand
                1+1
            elif lexerlib.isAssignation(word[0]):
                #check if word is an assignation
                1+1
    
    #write elements to file
    lexerlib.writeToFile("output.txt", "\N{LF}".join(elements))
    exit(0)
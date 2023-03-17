#read file and return a string with the content
def readFile(fileName):
    file = open(fileName, "r")
    content = file.read()
    file.close()
    return content

#write a string to a file
def writeToFile(fileName, content):
    file = open(fileName, "w")
    file.write(content)
    file.close()

#function that checks if a char is a letter
def isLetter(char):
    return char.isalpha()

#function that checks if a char is a digit
def isDigit(char):
    return char.isdigit()

#function that checks if a char is a bracket
def isBracket(char):
    return char in "()"

#function that checks if a char is an operand
def isOperand(char):
    return char in "+-*/^"

#checks if the first 2 elements of a string form a comment
def isComment(word):
    return word[0:2] == "//"

#checks if a char is an assignation
def isAssignation(char):
    return char == "="

#checks if a number is real or whole and if its valid
def validNumber(number):
    #check if it contains only numbers and dots
    for char in number:
        if not char.isdigit() and char != ".":
            return False
    #check if number is valid
    if not number.replace(".", "", 1).isdigit():
        return False
    #check if number is real
    if "." in number:
        return "real"
    #check if number is whole
    else:
        return "whole"
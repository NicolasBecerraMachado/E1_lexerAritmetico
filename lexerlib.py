import lexerState

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
def validNumber(number,state):
    #check if it contains only numbers and dots
    for char in number:
        if not char.isdigit() and char != ".":
            #assume error
            state.previous = "error"
            return False
    #check if number is valid
    if not number.replace(".", "", 1).isdigit():
        #assume error
        state.previous = "error"
        return False
            
    if state.previous == "number":
        state.previous = "number"
        return "error: consecutive numbers"
    if state.previous == "variable":
        state.previous = "number"
        return "error: number after variable"

    #state that we have a valid number
    state.number = True
    state.previous = "number"
    
    #check if number is real
    if "." in number:
        return "real"
    #check if number is whole
    else:
        return "whole"
    
#checks if a string is a valid assignation
def validAssignation(word, state):
    #check if word is an assignation
    if word != "=":
        #assume error
        state.previous = "error"
        return False
    #check if previous element was a number
    if state.number:
        #assume error
        state.previous = "error"
        return False
    #check if previous element was a variable
    if state.variable:
        #assume error
        state.previous = "error"
        return False
    
    if state.previous == "None":
        state.previous = "assignation"
        return "error: assignation at the beginning"
    if state.previous == "assignation":
        state.previous = "assignation"
        return "error: consecutive assignations"
    if state.previous == "operand":
        state.previous = "assignation"
        return "error: assignation after operand"
    

    #valid assignation
    state.previous = "assignation"

    #check if previous element was an operand
    state.asignation = True
    return "valid"    
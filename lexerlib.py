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
    #check if it contains only numbers and dots or scientific notation
    for char in number:
        if not char.isdigit() and char != "." and char != "e" and char != "E" and char != "-":
            #assume error
            state.previous = "error"
            print("error: invalid number - contains invalid characters")
            return False
    #check if number is valid
    if not number.replace(".", "", 1).replace("e", "", 1).replace("E", "", 1).replace("-", "", 1).isdigit():
        #assume error
        state.previous = "error"
        print("error: invalid number - contains extra dots or scientific notation or negative sign") 
        return False
                
    if state.previous == "number":
        state.previous = "number"
        print("error: number after number")
        return False
    if state.previous == "variable":
        state.previous = "number"
        print("error: number after variable")
        return False

    #state that we have a valid number
    state.number = True
    state.previous = "number"
    
    #check if number is a valid scientific notation
    if "e" in number or "E" in number:
        #check if number is valid
        if "e" in number:
            if not number.replace("e", "", 1).replace(".", "", 1).replace("-","",1).isdigit():
                #assume error
                print("invalid scientific")
                return False
        if "E" in number:
            if not number.replace("E", "", 1).replace(".", "", 1).replace("-","",1).isdigit():
                #assume error
                print("invalid scientific")
                return False
        #check if is number is real or whole
        #check how many times does the exponent increase the number
        if "e" in number:
            exponent = int(number.split("e")[1])
        if "E" in number:
            exponent = int(number.split("E")[1])
        #check if exponent is negative
        if exponent < 0:
            return "real"
        if not "." in number:
            return "whole"
        #check if positive exponent is enough to make the number whole
        if exponent >= len(number.split(".")[1]):
            return "whole"
        else:
            return "real"
        print("unrecognized scientific")
        return False

    #check if number is real
    if "." in number:
        return "real"
    #check if number is whole
    else:
        return "whole"   

#checks if a number is real or whole and if its valid
#exactly the same as valid number but allows number after number
def validNegNumber(number,state):
    #check if it contains only numbers and dots or scientific notation
    for char in number:
        if not char.isdigit() and char != "." and char != "e" and char != "E" and char != "-":
            #assume error
            state.previous = "error"
            print("error: invalid number - contains invalid characters")
            return False
    #check if number is valid
    if not number.replace(".", "", 1).replace("e", "", 1).replace("E", "", 1).replace("-", "", 1).isdigit():
        #assume error
        state.previous = "error"
        print("error: invalid number - contains extra dots or scientific notation or negative sign") 
        return False
    
    if state.previous == "variable":
        state.previous = "number"
        print("error: number after variable")
        return False

    #state that we have a valid number
    state.number = True
    state.previous = "number"
    
    #check if number is a valid scientific notation
    if "e" in number or "E" in number:
        #check if number is valid
        if "e" in number:
            if not number.replace("e", "", 1).replace(".", "", 1).replace("-","",1).isdigit():
                #assume error
                print("invalid scientific")
                return False
        if "E" in number:
            if not number.replace("E", "", 1).replace(".", "", 1).replace("-","",1).isdigit():
                #assume error
                print("invalid scientific")
                return False
        #check if is number is real or whole
        #check how many times does the exponent increase the number
        if "e" in number:
            exponent = int(number.split("e")[1])
        if "E" in number:
            exponent = int(number.split("E")[1])
        #check if exponent is negative
        if exponent < 0:
            return "real"
        if not "." in number:
            return "whole"
        #check if positive exponent is enough to make the number whole
        if exponent >= len(number.split(".")[1]):
            return "whole"
        else:
            return "real"
        print("unrecognized scientific")
        return False

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
        print ("error: assignation at the beginning")
        return "False"
    if state.previous == "assignation":
        state.previous = "assignation"
        print ("error: consecutive assignations")
        return False
    if state.previous == "operand":
        state.previous = "assignation"
        print("error: assignation after operand")
        return False
    

    #valid assignation
    state.previous = "assignation"

    #check if previous element was an operand
    state.asignation = True
    return "valid"

#checks if a string is a valid variable
def validVariable(word, state):
    #check if word is a variable
    if not word.replace("_","").isalnum():
        #assume error
        state.previous = "error"
        print("error: invalid variable - contains invalid characters")
        return False
    #check if previous element was a number
    if state.previous == "number":
        #assume error
        state.previous = "error"
        print("error: variable after number")
        return False
    #check if previous element was a variable
    if state.previous == "variable":
        #assume error
        state.previous = "error"
        print("error: consecutive variables")
        return False
    
    if state.previous == "None":
        state.previous = "variable"
        return "variable"
    if state.previous == "assignation":
        state.previous = "variable"
        return "variable"
    if state.previous == "operand":
        state.previous = "variable"
        return "variable"
    
    #valid variable
    state.previous = "variable"
    state.variable = True
    return "variable"

#checks if a string is a valid operand
def validOperand(word, state):
    #check if handling a negative number
    if word[0] == "-" and len(word) > 1:
        stateP = validNegNumber(word[1:], state)
        if stateP == "whole":
            state.previous = "number"
            state.number = True
            return "whole"
        if stateP == "real":
            state.previous = "number"
            state.number = True
            return "real"
        else:
            print("error: invalid negative number")
            return "false number"
    #check if word is an operand
    if word not in "+-*/^":
        #assume error
        state.previous = "error"
        print("error: invalid operand")
        return False
    #check if previous element was a open bracket
    if state.previous == "open bracket":
        #assume error
        state.previous = "error"
        print("error: operand after open bracket")
        return False
    #check if previous element was an operand
    if state.previous == "operand":
        #assume error
        state.previous = "error"
        print("error: consecutive operands")
        return False
    #check if previous element was an assignation
    if state.previous == "assignation":
        #assume error
        state.previous = "error"
        print("error: operand after assignation")
        return False
    
    if state.previous == "None":
        state.previous = "operand"
        print ("error: operand at the beginning")
        return "False"
    
    #valid operand
    state.previous = "operand"
    state.operand = True
    return "operand"

#inserts a bracket in stack
def insertBracket(state):
    #valid bracket
    state.previous = "open bracket"
    state.addBracket("(")
    return "valid"

#remove a bracket from stack
def removeBracket(state):

    #check if stack is empty
    if(state.getLastBracket() != "("):
        state.previous = "close bracket"
        print("error: invalid bracket")
        return "invalid"

    if(state.previous == "open bracket"):
        state.previous = "close bracket"
        print("error: empty bracket")
        return "invalid"
    
    if(state.previous == "operand"):
        state.previous = "close bracket"
        print("error: close bracket after operand")
        return "invalid"


    #valid bracket
    state.previous = "close bracket"
    state.removeBracket()
    return "valid"
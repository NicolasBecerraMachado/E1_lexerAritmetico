import os
import sys
import lexerlib
import lexerState

#function to contain functionality of the lexer
def lexerAritmetico(filename):
    #read file
    content = lexerlib.readFile(fileName)

    #split content by lines
    lines = content.split("\N{LF}")

    #will store the identified and labeled elements
    elements = []

    #variables used to identify the state
    stateLexer = lexerState.lexerState()

    #iterate through lines
    for line in lines:
        #add a space before and after each operand or assignation
        line = line.replace("+", " + ")
        #check if minus is a operand or a exponent in scientific notation or a negative number
        i = 0
        #check if we do not begin with a negative number
        if line and line[0] == "-":
            if not (len(line) > 1 and line[1].isdigit()):
                line = " - " + line[1:]
                i+=2
        while i < len(line):
            #check if is allowed to split or scientific notation
            if line[i] == "-" and i != 0 and (line[i-1] == "e" or line[i-1] == "E") and line[i+1].isdigit():
                1+1
            elif line[i] == "-" and i != len(line)-1 and line[i+1].isdigit():
                line = line[:i] + " -" + line[i+1:]
                i+=1
            elif line[i] == "-":
                line = line[:i] + " - " + line[i+1:]
                i+=2
            if i == len(line)-1 and line[i] == "-":
                line = line[:i] + " - "
                i+=2
            i += 1
        line = line.replace("*", " * ")
        line = line.replace("//", " // ")
        #check if slash is a operand and not an comment
        i = 0
        while i < len(line):
            if line[i] == "/" and i != len(line)-1 and line[i+1] != "/":
                line = line[:i] + " / " + line[i+1:]
                i+=2
            elif line[i] == "/" and i != len(line)-1 and line[i+1] == "/":
                #skip next element
                break
            i += 1
        line = line.replace("^", " ^ ")
        line = line.replace("=", " = ")
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")

        #split line by spaces
        words = line.split(" ")

        for word in words:
            if len(word) == 0:
                continue
            #create case based on firs element of word
            if lexerlib.isLetter(word[0]):
                #check if word is a variable
                state = lexerlib.validVariable(word,stateLexer)
                if state == "variable":
                    elements.append([word,"variable"])
                else:
                    elements.append([word,"invalid variable"])
                    print("Invalid variable in line: " + line)

            elif lexerlib.isDigit(word[0]):
                #check if word is a number
                state = lexerlib.validNumber(word,stateLexer)
                if state == "real":
                    elements.append([word,"real number"])
                elif state == "whole":
                    elements.append([word,"whole number"])
                else:
                    elements.append([word,"invalid number"])
                    print("Invalid number in line: " + line)
            
            elif lexerlib.isBracket(word[0]):
                #check if word is a bracket
                if(word[0] == "("):
                    state = lexerlib.insertBracket(stateLexer)
                    if state == "valid":
                        elements.append([word,"open bracket"])
                else:
                    state = lexerlib.removeBracket(stateLexer)
                    if state == "valid":
                        elements.append([word,"close bracket"])
                    else:
                        elements.append([word,"invalid bracket"])
                        print("Invalid bracket in line: " + line)
                
            
            elif lexerlib.isComment(word):
                #check if word is a comment
                elements.append([word,"comment"])
                break
                
            elif lexerlib.isOperand(word[0]):
                #check if word is an operand
                state = lexerlib.validOperand(word,stateLexer)
                if state == "operand":
                    elements.append([word,"operand"])
                elif state == "whole":
                    elements.append([word,"whole number"])
                elif state == "real":
                    elements.append([word,"real number"])
                elif state == "false number":
                    elements.append([word,"invalid number"])
                    print("Invalid number in line: " + line)
                else:
                    elements.append([word,"invalid operand"])
                    print("Invalid operand in line: " + line)
            
            elif lexerlib.isAssignation(word[0]):
                #check if word is an assignation
                state = lexerlib.validAssignation(word,stateLexer)
                if state == "valid":
                    elements.append([word,"assignation"])
                else:
                    elements.append([word,"invalid assignation"])
                    print("Invalid assignation in line: " + line)



        elements.append(["////////","line break"])
        stateLexer.resetState()
    
    #write elements to file
    #write each element in a new line
    content = ""
    for element in elements:
        content += element[0] + "           " + element[1] + "\N{LF}"
    lexerlib.writeToFile("output.txt", content)

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
    
    #call lexer function
    lexerAritmetico(fileName)

    exit(0)
#create class to store the state of the lexer
class lexerState:
    #constructor
    def __init__(self):
        #variables used to identify the state
        self.operand = False
        self.asignation = False
        self.comment = False
        self.variable = False
        self.number = False
        self.bracket = False
        self.previous = "None"
        self.stack = []

    #reset the state when change of line
    def resetState(self):
        self.operand = False
        self.asignation = False
        self.comment = False
        self.variable = False
        self.number = False
        self.bracket = False
        self.previous = "None"
        self.stack = []
    
    #adds a bracket to the stack
    def addBracket(self, bracket):
        self.stack.append(bracket)
    
    #removes a bracket from the stack
    def removeBracket(self):
        self.stack.pop()
    
    #returns the last bracket in the stack
    def getLastBracket(self):
        return self.stack[-1]
    
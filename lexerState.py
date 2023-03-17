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

    #reset the state when change of line
    def resetState(self):
        self.operand = False
        self.asignation = False
        self.comment = False
        self.variable = False
        self.number = False
        self.bracket = False
        self.previous = "None"
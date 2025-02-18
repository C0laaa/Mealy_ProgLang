class MealyMachine:
    def __init__(self, states, inputs, outputs, initialState):
        self.states = states
        self.inputs = inputs
        self.outputs = outputs
        self.transitions = {}
        self.currentState = initialState

    def addTransition(self, currentState, inputSymbol, nextState, outputSymbol):
        self.transitions[(currentState, inputSymbol)] = (nextState, outputSymbol)

    def transition(self, inputSymbol):
        if (self.currentState, inputSymbol) in self.transitions:
            nextState, output = self.transitions[(self.currentState, inputSymbol)]
            self.currentState = nextState
            return output
        else:
            return None

    def get_currentState(self):
        return self.currentState

states = input("Enter the states (space-separated): ").split(' ')
inputs = input("Enter the inputs (space-separated): ").split(' ')
outputs = input("Enter the outputs (space-separated): ").split(' ')
initialState = input("Enter the initial state: ")

mealyMachine = MealyMachine(states, inputs, outputs, initialState)

num_transitions = int(input("Enter the number of transitions: "))
for _ in range(num_transitions):
    currentState = input("Enter current state: ")
    inputSymbol = input("Enter input symbol: ")
    nextState = input("Enter next state: ")
    outputSymbol = input("Enter output symbol: ")
    mealyMachine.addTransition(currentState, inputSymbol, nextState, outputSymbol)

while True:
    inputSequence = input("Enter the input sequence (or type 'exit' to quit): ")
    if inputSequence.lower() == 'exit':
        break

    outputSequence = ""
    for symbol in inputSequence:
        output = mealyMachine.transition(symbol)
        if output is not None:
            outputSequence += output

    print("Input Sequence:", inputSequence)
    print("Output Sequence:", outputSequence)

    # Reset the current state for the next input sequence
    mealyMachine.currentState = initialState
print("Exiting the program.")
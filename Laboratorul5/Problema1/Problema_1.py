class MooreMachine:
    def __init__(self):
        self.state = 'S1'

    def transition(self, input):
        if self.state == 'S1':
            if input == 'A':
                self.state = 'S1'
                return 'O1'
            elif input == 'B':
                self.state = 'S2'
                return 'O1'
        elif self.state == 'S2':
            if input == 'A':
                self.state = 'S1'
                return 'O2'
            elif input == 'B':
                self.state = 'S2'
                return 'O2'

    def reset(self):
        self.state = 'S1'

# Exemplu de utilizare
moore_machine = MooreMachine()
inputs = ['A', 'B', 'A', 'B', 'A']
for inp in inputs:
    output = moore_machine.transition(inp)
    print(f'Intrare: {inp}, Ieșire: {output}')

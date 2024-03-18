class MealyMachine:
    def __init__(self):
        self.state = 'Q1'

    def transition(self, input):
        if self.state == 'Q1':
            if input == 'X':
                self.state = 'Q2'
                return 'O1'
            elif input == 'Y':
                return 'O1'
        elif self.state == 'Q2':
            if input == 'X':
                return 'O2'
            elif input == 'Y':
                self.state = 'Q2'
                return 'O2'

    def reset(self):
        self.state = 'Q1'

# Exemplu de utilizare
mealy_machine = MealyMachine()
inputs = ['X', 'Y', 'X', 'Y', 'X']
for inp in inputs:
    output = mealy_machine.transition(inp)
    print(f'Intrare: {inp}, Ieșire: {output}')

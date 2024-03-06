class NFA:
    def __init__(self):
        self.states = {'S0', 'S1', 'S2', 'S3'}
        self.accept_state = {'S1'}
        self.alphabet = {'a', 'b'}

    def delta(self, state, symbol):
        transitions = {
            'S0': {'a': {'S2'}, 'b': {'S3'}},
            'S1': {},
            'S2': {'a': {'S2'}, 'b': {'S1'}},
            'S3': {'a': {'S1'}, 'b': {'S3'}}
        }
        return transitions.get(state, {}).get(symbol, set())

    def is_accepted(self, state):
        return state in self.accept_state

nfa = NFA()
print("Tranzitiile pentru S0 cu a:", nfa.delta('S0', 'a'))  # {'S2'}
print("Starea S1 este starea de acceptare:", nfa.is_accepted('S1'))  # True

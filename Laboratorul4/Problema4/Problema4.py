class NFA:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_states = {initial_state}
        self.accepting_states = accepting_states

    def reset(self):
        self.current_states = {self.initial_state}

    def transition(self, symbol):
        next_states = set()
        for state in self.current_states:
            if (state, symbol) in self.transitions:
                next_states.update(self.transitions[(state, symbol)])
        self.current_states = next_states

    def is_accepted(self):
        return bool(self.current_states.intersection(self.accepting_states))


# Exemplu de utilizare
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {('q0', 'a'): {'q1'},
               ('q1', 'b'): {'q2'},
               ('q2', 'a'): {'q0', 'q1'}}
initial_state = 'q0'
accepting_states = {'q2'}

nfa = NFA(states, alphabet, transitions, initial_state, accepting_states)
nfa.transition('a')
nfa.transition('b')
nfa.transition('a')
print("Starea curentă:", nfa.current_states)
print("Este acceptat:", nfa.is_accepted())

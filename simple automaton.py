class FiniteStateMachine:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}  
        self.alphabet = {'a', 'b'}  
        self.transitions = {  
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q0'
        }
        self.start_state = 'q0'  
        self.accept_states = {'q2'}  

    def recognize(self, string):
        current_state = self.start_state
        for char in string:
            if (current_state, char) in self.transitions:
                current_state = self.transitions[(current_state, char)]
            else:
                return False  

        return current_state in self.accept_states


def main():
    fsm = FiniteStateMachine()

    test_strings = ['ab', 'aab', 'abb', 'aaaab', 'baab', 'bba', 'abab']
    for string in test_strings:
        if fsm.recognize(string):
            print(f"'{string}' is accepted")
        else:
            print(f"'{string}' is rejected")


if __name__ == "__main__":
    main()

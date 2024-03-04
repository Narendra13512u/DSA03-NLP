def parse(input_str, grammar):
    chart = [[] for _ in range(len(input_str) + 1)]

    def predict(state, chart):
        for rule in grammar[state.next_symbol()]:
            chart[state.end_index].append(State(state.next_symbol(), rule, state.start_index, state.start_index))

    def scan(state, chart):
        if state.next_symbol() == input_str[state.end_index]:
            chart[state.end_index + 1].append(State(state.next_symbol(), state.rule, state.start_index, state.start_index + 1))

    def complete(state, chart):
        for st in chart[state.start_index]:
            if st.next_symbol() == state.rule[0] and st.end_index == state.start_index:
                chart[state.end_index].append(State(st.next_symbol(), st.rule, st.start_index, state.start_index))

    class State:
        def _init_(self, symbol, rule, start_index, end_index):
            self.symbol = symbol
            self.rule = rule
            self.start_index = start_index
            self.end_index = end_index

        def next_symbol(self):
            if len(self.rule) > 1:
                return self.rule[1]
            return None

    start_state = State(grammar['S'][0][0], grammar['S'][0], 0, 0)
    chart[0].append(start_state)

    for i in range(len(input_str) + 1):
        for state in chart[i]:
            if state.next_symbol() is not None:
                if state.next_symbol() in grammar:
                    predict(state, chart)
                else:
                    scan(state, chart)
            else:
                complete(state, chart)

    for state in chart[-1]:
        if state.symbol == 'S' and state.start_index == 0:
            return True
    return False


# Example usage:
grammar = {
    'S': [['A', 'B']],
    'A': [['a'], ['']],
    'B': [['b']]
}
input_str = 'ab'
print(parse(input_str, grammar))  # Output: True

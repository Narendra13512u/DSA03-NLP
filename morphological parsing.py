class PluralFiniteStateMachine:
    def __init__(self):
        self.singular_suffixes = ['s', 'x', 'ch', 'sh', 'o']  
        self.irregular_forms = {'man': 'men', 'woman': 'women', 'child': 'children'} 

    def generate_plural(self, noun):
        if noun in self.irregular_forms:
            return self.irregular_forms[noun]
        elif noun[-1] in self.singular_suffixes:
            return noun + 'es'
        else:
            return noun + 's'


def main():
    fsm = PluralFiniteStateMachine()

    test_nouns = ['dog', 'cat', 'fox', 'box', 'church', 'tomato', 'child', 'woman', 'man']
    for noun in test_nouns:
        plural = fsm.generate_plural(noun)
        print(f"Singular: {noun}, Plural: {plural}")


if __name__ == "__main__":
    main()

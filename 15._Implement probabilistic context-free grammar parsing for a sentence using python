import nltk

# Define a probabilistic context-free grammar
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | NP PP [0.3]
    VP -> V NP [0.4] | VP PP [0.6]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'cat' [0.5] | 'dog' [0.5]
    V -> 'chased' [0.7] | 'ate' [0.3]
    P -> 'on' [0.6] | 'in' [0.4]
""")

# Create a parser based on the PCFG
parser = nltk.ViterbiParser(pcfg_grammar)

# Input sentence to parse
sentence = "the cat chased the dog"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence using the PCFG parser
for tree in parser.parse(tokens):
    tree.pretty_print()

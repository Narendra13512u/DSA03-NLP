import nltk

# Define the context-free grammar
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
    P -> 'on' | 'in'
""")

# Create a parser based on the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to parse
sentence = "the cat chased the dog"

# Tokenize the sentence
tokens = sentence.split()

# Generate the parse tree
for tree in parser.parse(tokens):
    tree.pretty_print()

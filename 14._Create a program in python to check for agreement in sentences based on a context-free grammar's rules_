import nltk

# Define the context-free grammar with subject-verb agreement rules
grammar = nltk.CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> 'he' | 'she' | 'dog'
    NP_PL -> 'they' | 'cats'
    VP_SG -> V_SG | V_SG NP_SG
    VP_PL -> V_PL | V_PL NP_PL
    V_SG -> 'runs' | 'eats'
    V_PL -> 'run' | 'eat'
""")

# Create a parser based on the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to check for agreement
sentence = "he runs"

# Tokenize the sentence
tokens = sentence.split()

# Check for agreement by parsing the sentence
agreement = False
for tree in parser.parse(tokens):
    agreement = True

# Output the result of agreement check
if agreement:
    print("The sentence follows the subject-verb agreement rules.")
else:
    print("The sentence does not follow the subject-verb agreement rules.")

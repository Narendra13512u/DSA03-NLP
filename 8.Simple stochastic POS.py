import random


training_corpus = [
    ("I", "PRON"),
    ("love", "VERB"),
    ("to", "PART"),
    ("read", "VERB"),
    ("books", "NOUN"),
    ("in", "ADP"),
    ("the", "DET"),
    ("library", "NOUN"),
    (".", "PUNCT")
]

def build_pos_model(corpus):
    pos_model = {}
    for word, pos_tag in corpus:
        if pos_tag in pos_model:
            pos_model[pos_tag].append(word)
        else:
            pos_model[pos_tag] = [word]
    return pos_model

pos_model = build_pos_model(training_corpus)

def stochastic_pos_tagging(pos_model, words):
    tagged_words = []
    for word in words:
        if word in pos_model:
            pos_tag = random.choice(pos_model[word])
            tagged_words.append((word, pos_tag))
        else:
           
            tagged_words.append((word, "UNK"))
    return tagged_words

text = ["I", "love", "to", "read", "books", "in", "the", "library", "."]


tagged_text = stochastic_pos_tagging(pos_model, text)

print("Stochastic Part-of-Speech Tagging:")
for word, pos_tag in tagged_text:
    print(f"{word}: {pos_tag}")

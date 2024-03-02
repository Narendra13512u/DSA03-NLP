import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import nltk
from nltk.tokenize import word_tokenize


text = "I love to read books in the library."


words = word_tokenize(text)


pos_tags = nltk.pos_tag(words)


print("Part-of-Speech Tagging:")
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")


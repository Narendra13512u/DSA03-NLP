import nltk
text = "I love to read books in the library."
words = nltk.word_tokenize(text)
tagged_words = nltk.pos_tag(words)
transformation_rules = [
    (r'\blove\b', 'VB'), 
    (r'\bbooks\b', 'NNS')  
]
for i, (word, tag) in enumerate(tagged_words):
    for pattern, new_tag in transformation_rules:
        if nltk.re.match(pattern, word):
            tagged_words[i] = (word, new_tag)
            break
print("Transformation-Based Tagging:")
for word, tag in tagged_words:
    print(f"{word}: {tag}")

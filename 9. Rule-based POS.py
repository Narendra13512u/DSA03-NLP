import re

text = "I love to read books in the library."
pos_rules = [
    (r'\b(?:I|you|he|she|it|we|they)\b', 'PRON'),
    (r'\b(?:love|hate|like|read)\b', 'VERB'),
    (r'\b(?:to)\b', 'PART'),
    (r'\b(?:books|library)\b', 'NOUN'),
    (r'\b(?:in)\b', 'ADP'),
    (r'\b(?:the|a)\b', 'DET'),
    (r'\b(?:\.)\b', 'PUNCT')
]
def rule_based_pos_tagging(text, rules):
    tagged_text = []
    for word in text.split():
        tagged_word = None
        for regex_pattern, pos_tag in rules:
            if re.match(regex_pattern, word):
                tagged_word = (word, pos_tag)
                break
        if tagged_word is None:
            tagged_word = (word, 'UNK') 
        tagged_text.append(tagged_word)
    return tagged_text
tagged_text = rule_based_pos_tagging(text, pos_rules)
print("Rule-based Part-of-Speech Tagging using Regular Expressions:")
for word, pos_tag in tagged_text:
    print(f"{word}: {pos_tag}")

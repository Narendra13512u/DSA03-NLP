import random


sample_text = "I like to go for a walk in the park every morning. The birds chirp and the sun shines brightly."


def generate_bigrams(text):
    words = text.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    return bigrams


bigrams = generate_bigrams(sample_text)


def build_bigram_model(bigrams):
    bigram_model = {}
    for word1, word2 in bigrams:
        if word1 in bigram_model:
            bigram_model[word1].append(word2)
        else:
            bigram_model[word1] = [word2]
    return bigram_model


bigram_model = build_bigram_model(bigrams)


def generate_text(bigram_model, start_word, num_words=10):
    text = [start_word]
    current_word = start_word
    for _ in range(num_words-1):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(text)


generated_text = generate_text(bigram_model, 'I', num_words=15)
print(generated_text)

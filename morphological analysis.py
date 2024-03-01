import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def morphological_analysis(text):
    tokens = word_tokenize(text)
    for token in tokens:
        synsets = wordnet.synsets(token)
        if synsets:
            print("Token:", token)
            for synset in synsets:
                print("Lemma:", synset.lemmas()[0].name())
                print("POS Tag:", synset.pos())
                print("Definition:", synset.definition())
                print()

def main():
    nltk.download('punkt')
    nltk.download('wordnet')

    text = "The quick brown fox jumps over the lazy dog"
    print("Performing morphological analysis on text:", text)
    print("-----------------------------------------------")
    morphological_analysis(text)

if __name__ == "__main__":
    main()

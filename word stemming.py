import nltk
from nltk.stem import PorterStemmer

def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

def main():
    nltk.download('punkt')

    words = ["running", "runs", "runner", "ran", "easily", "fairly", "fairness"]
    print("Original words:", words)

    stemmed_words = stem_words(words)
    print("Stemmed words:", stemmed_words)

if __name__ == "__main__":
    main()

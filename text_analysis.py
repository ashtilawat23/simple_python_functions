# complex_function.py

import re
from collections import Counter

def analyze_text(text):
    """
    Analyzes the given text and returns statistics about word frequency,
    sentence count, and the longest word.

    :param text: str, input text to be analyzed
    :return: dict, statistics about the text
    """
    # Remove punctuation and make lowercase
    clean_text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split text into words
    words = clean_text.split()
    
    # Count word frequency
    word_freq = Counter(words)
    
    # Split text into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Find the longest word
    longest_word = max(words, key=len) if words else ''
    
    # Prepare statistics
    stats = {
        'word_count': len(words),
        'sentence_count': len(sentences),
        'most_common_words': word_freq.most_common(5),
        'longest_word': longest_word
    }
    
    return stats

def main():
    text = (
        "Hello world! This is a test text. "
        "Python programming is fun. "
        "Complex functions can be interesting to write and understand."
    )
    
    stats = analyze_text(text)
    print("Text Analysis Statistics:")
    print(f"Word Count: {stats['word_count']}")
    print(f"Sentence Count: {stats['sentence_count']}")
    print(f"Most Common Words: {stats['most_common_words']}")
    print(f"Longest Word: {stats['longest_word']}")

if __name__ == "__main__":
    main()

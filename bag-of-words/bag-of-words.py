import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    bow_vector = np.zeros(len(vocab), dtype = int)

    word_to_idx = {word: i for i,word in enumerate(vocab)}

    for word in tokens:
        if word in word_to_idx:
            idx = word_to_idx[word]
            bow_vector[idx] += 1
    return bow_vector
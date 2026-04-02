def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    word_freq = {}

    for sentence in sentences:
        for token in sentence:
            word_freq[token] = word_freq.get(token, 0) + 1
    return word_freq
    pass
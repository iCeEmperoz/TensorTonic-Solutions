import numpy as np

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    n = len(actual_tokens)
    log_probs = []

    for i in range(n):
        prob_actual = prob_distributions[i][actual_tokens[i]]

        log_probs.append(np.log(prob_actual + 1e-10))

    cross_entropy = -np.mean(log_probs)

    perplexity = np.exp(cross_entropy)

    return perplexity
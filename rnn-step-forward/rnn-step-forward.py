import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    input_part = np.dot(x_t, Wx)

    hidden_part = np.dot(h_prev, Wh)

    h_t = np.tanh(input_part + hidden_part + b)

    return h_t
    pass

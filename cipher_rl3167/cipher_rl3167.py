def cipher(text, shift, encrypt=True):
    """
    This is a function to encode and decode texts.
    Each letter is replaced by a letter some fixed number of positions down the alphabet.

    Parameters (Inputs)
    ----------
    text : str
        A string of texts to encrypt or decrypt.
    shift : int
        An integer representing how many digits of position you want the texts to be shifted.
    encrypt : boolean
        A boolean stating the choice encrypt (if = True) or decrypt (if = False).

    Returns (Output)
    -------
    str
        A string of the encrypt or decrypt result of the input text.

    Examples
    --------
    >>> from cipher_rl3167 import cipher_rl3167
    >>> text = "I love MDS"
    >>> shift = 1
    >>> cipher_rl3167.cipher(text, shift, encrypt = True)
    'J mpwf NET'
    >>> text = "J mpwf NET"
    >>> cipher_rl3167.cipher(text, shift, encrypt = False)
    'I love MDS'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

import string


def get_words(in_text):
    """
    Problem 1

    This function takes string as input and returns words list
    """

    return in_text.split()


def get_clean_words(in_text):
    """
    Problem 2

    This function takes string as input and returns  lowercase words list
    removing punctuations and numbers
    """

    in_text = in_text.translate(None, string.punctuation + string.digits)
    return in_text.lower().split()

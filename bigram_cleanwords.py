import string


def get_bigrams(in_text):
    """
    Problem 7

    This function takes string as input and returns bigram list
    """

    text_list = in_text.split()
    bigram_list = []
    for i in range(len(text_list)-1):
        bigram_list.append((text_list[i], text_list[i+1]))
    return bigram_list


def get_clean_bigrams(in_text):
    """
    Problem 7

    This function takes string as input and returns  lowercase bigram list
    removing punctuations and numbers
    """

    in_text = in_text.lower().translate(None, string.punctuation + string.digits)
    return get_bigrams(in_text)

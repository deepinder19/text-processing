from bigram_cleanwords import get_clean_bigrams, get_bigrams
from cleanwords import get_clean_words


def bigram_freq(file_path):
    """
    Problem 7

    This functions returns count of bigrams from text file
    """

    with open(file_path, 'r') as f_obj:
        bigram_list = get_clean_bigrams(f_obj.read())
    freq_dict = {bigram: bigram_list.count(bigram) for bigram in bigram_list}
    return freq_dict


def bigram_freq2(file_path1, file_path2):
    """
    Problem 7

    This functions returns count of words from text file
    eliminating noise words from other file
    """

    with open(file_path1, 'r') as f_obj:
        word_list = get_clean_words(f_obj.read())
    with open(file_path2, 'r') as n_obj:
        noise_list = n_obj.read().split()
    new_list = [word for word in word_list if word not in noise_list]
    bigram_list = get_bigrams(" ".join(new_list))
    freq_dict = {bigram: bigram_list.count(bigram) for bigram in bigram_list}
    return freq_dict

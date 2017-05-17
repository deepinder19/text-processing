from cleanwords import get_clean_words


def word_freq(file_path):
    """
    Problem 3

    This functions returns count of words from text file
    """

    with open(file_path, 'r') as f_obj:
        word_list = get_clean_words(f_obj.read())
    freq_dict = {word: word_list.count(word) for word in word_list}
    return freq_dict


def word_freq2(file_path1, file_path2):
    """
    Problem 4

    This functions returns count of words from text file
    eliminating noise words from other file
    """

    with open(file_path1, 'r') as f_obj:
        word_list = get_clean_words(f_obj.read())
    with open(file_path2, 'r') as n_obj:
        noise_list = n_obj.read().split()
    freq_dict = {word: word_list.count(word) for word in word_list if word not in noise_list}
    return freq_dict

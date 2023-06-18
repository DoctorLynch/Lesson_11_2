def foo(word):
    """
    Docstring
    :param word:
    :return:
    """
    return word.upper()


def foo2(word):
    """

    :param word:
    :return:
    """
    word_list = word.split()
    result = []
    for word in word_list:
        result.append(word.capitalize())
    return ' '.join(result)
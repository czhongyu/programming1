from nltk.tokenize import sent_tokenize


def strings_in_both(strings_a, strings_b):
    # find strings that exist in both string list
    # dictionary counter
    count = {}
    # string list
    strings = []
    # mark strings in string list a
    for string in strings_a:
        count[string] = 1
    # mark strings in string list b
    for string in strings_b:
        if string in count:
            count[string] += 1
    # find all the strings that exist in both list
    for key in count:
        if count[key] > 1:
            strings.append(key)
    return strings


def split_into_substrings(string, n):
    # split string into substrings with length n
    substrings = []
    length = len(string)
    # split
    for i in range(length - n + 1):
        substrings.append(string[i: i + n])

    return substrings


def lines(a, b):
    """Return lines in both a and b"""

    lines_a = a.split('\n')
    lines_b = b.split('\n')
    # find strings in both list
    return strings_in_both(lines_a, lines_b)


def sentences(a, b):
    """Return sentences in both a and b"""

    sents_a = sent_tokenize(a)
    sents_b = sent_tokenize(b)
    # find strings in both list
    return strings_in_both(sents_a, sents_b)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    substrings_a = split_into_substrings(a, n)
    substrings_b = split_into_substrings(b, n)
    # find strings in both list
    return strings_in_both(substrings_a, substrings_b)
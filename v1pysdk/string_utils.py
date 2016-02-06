def split_attribute(attribute_string):
    """
    Properly split apart attribute strings, even when they have sub-attributes
    declated between [].
    Sub-attribute strings between '[]'s are appended to their parent, without
    processing, even if they contain '.'

    :param attribute_string:the attribute string to split
    :return: dict containing the elements of the top level attribute string.
    """
    ret = []
    # zero means we are not inside square brackets
    square_brackets = 0
    last_index = 0
    a_len = len(attribute_string)

    for i in range(a_len):
        if attribute_string[i] == '[':
            square_brackets += 1
        elif attribute_string[i] == ']':
            square_brackets -= 1
        elif attribute_string[i] == '.' and square_brackets == 0:
            ret.append(attribute_string[last_index:i])
            last_index = i + 1

    # last element
    ret.append(attribute_string[last_index:])
    return ret

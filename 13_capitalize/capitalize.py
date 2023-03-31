def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    char = phrase[0]
    upper_char = char.upper()
    return phrase.replace(char, upper_char, 1)
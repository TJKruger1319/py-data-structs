def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    v = True
    new_string = ""
    for char in phrase:
        if (char == " "):
            v = True
            new_string += char
        elif (char != ' ' and v == True):
            new_string += char.upper()
            v = False
        else:
            new_string += char.lower()
    return new_string
def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_string = ""
    for element in phrase:
        if element == to_swap.lower():
            swapped_element = element.swapcase()
            new_string += swapped_element
        elif element == to_swap.upper():
            swapped_element = element.swapcase()
            new_string += swapped_element
        else:
            new_string += element
    return new_string
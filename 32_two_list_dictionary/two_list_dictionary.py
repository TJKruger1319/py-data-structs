def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    dic = dict()
    i = 0
    key_length = len(keys)
    values_length = len(values)
    if key_length <= values_length:
        for key in keys:
            dic[key] = values[i]
            i += 1
    else:
        for x in range(0 , len(keys)-len(values)):
            values.append(None)
        for value in values:
            dic[keys[i]] = value
            i += 1
    return dic

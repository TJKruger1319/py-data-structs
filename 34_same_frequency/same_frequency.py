def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_num1 = str(num1)
    str_num2 = str(num2)
    for x in range(0, len(str_num1)):
        i = str_num1[x]
        if str_num1.count(i) != str_num2.count(i):
            return False
    return True

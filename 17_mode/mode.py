def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    highest = 0
    winner = 0
    for element in nums:
        temp_highest = nums.count(element)
        if temp_highest > highest:
            highest = temp_highest
            winner = element
    return winner

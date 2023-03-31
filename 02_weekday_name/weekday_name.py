def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    weekdays = ["None", "Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","None"]
    if day_of_week in range(0,8):
        return weekdays[day_of_week]
    else:
        return "None"

print(weekday_name(1))
print(weekday_name(9))
print(weekday_name(6))
print(weekday_name(4))
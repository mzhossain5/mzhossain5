def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    # Carry over seconds if greater than 59
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    
    # Carry over minutes if greater than 59
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    
    # Ensure hours are within 0-23
    sum.hour = sum.hour % 24
    
    return sum

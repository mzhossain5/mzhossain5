#!/usr/bin/env python3
# Student ID: [134746221]
from lab7d import *

t1 = Time(9, 50, 0)
print(t1)            # This will print something like '<lab7d.Time object at 0x7f1232a79be0>'
print(t1.format_time())  # Use the method to format time
print(t1.valid_time())   # Test the validity check method

t2 = Time(8, 55, 0)
tsum = t1.sum_times(t2)
print(tsum.format_time())  # Sum two times and format the result

t3 = Time(9, 50, 0)
t3.change_time(1800)
print(t3.format_time())  # Change time by adding seconds and format the result


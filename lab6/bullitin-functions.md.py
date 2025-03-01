#esep 1

from functools import reduce

numbers = [2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)

print(result)

#esep 2

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

text = "Hello World"
upper_count, lower_count = count_case(text)

print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)

#esep 3

def is_palindrome(s):
    return s == s[::-1]

text = "madam"
print(is_palindrome(text))

#esep 4

import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

num = 25100
delay = 2123

result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")

#esep 5

def all_true(t):
    return all(t)

t = (True, True, False)
print(all_true(t))

#esep 1 
import re

def match_pattern(s):
    return bool(re.fullmatch(r"a*b*", s))

test_strings = ["a", "ab", "abb", "abbb", "ac", "b", "ba", "abc"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#esep 2

import re

def match_pattern(s):
    return bool(re.fullmatch(r"ab{2,3}", s))

test_strings = ["abb", "abbb", "a", "ab", "abbbb", "abc", "abba"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#esep 3

import re

def match_pattern(s):
    return bool(re.fullmatch(r"[a-z]+_[a-z]+", s))

test_strings = ["hello_world", "test_case", "Python_programming", "helloWorld", "test_", "_case"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#esep 4

import re

def match_pattern(s):
    return bool(re.fullmatch(r"[A-Z][a-z]+", s))

test_strings = ["Hello", "Test", "Python", "JAVA", "java", "C", "Test123"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#esep 5

import re

def match_pattern(s):
    return bool(re.fullmatch(r"a.*b", s))

test_strings = ["ab", "acb", "a123b", "axb", "a", "b", "abc", "a_b"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#esep 6 

import re

def replace_characters(s):
    return re.sub(r"[ ,.]", ":", s)

test_strings = ["Hello, world. How are you?", "Python is great.", "This is a test, isn't it?"]
for s in test_strings:
    print(replace_characters(s))
 
 #esep 7

 import re

def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), s)

test_strings = ["hello_world", "convert_this_string", "snake_case_example"]
for s in test_strings:
    print(snake_to_camel(s))

#esep 8

import re

def split_at_uppercase(s):
    return re.split(r"(?=[A-Z])", s)

test_strings = ["HelloWorld", "SplitAtUpperCase", "PythonProgramming"]
for s in test_strings:
    print(split_at_uppercase(s))

#esep 9

import re

def insert_spaces(s):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", s)


test_strings = ["HelloWorld", "InsertSpacesBetweenWords", "PythonIsFun"]
for s in test_strings:
    print(insert_spaces(s))

#esep 10

import re

def camel_to_snake(s):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", s).lower()

test_strings = ["HelloWorld", "ConvertThisString", "CamelCaseExample"]
for s in test_strings:
    print(camel_to_snake(s))


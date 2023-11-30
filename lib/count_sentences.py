#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self._value:
            return self._value.endswith('.')
        return False

    def is_question(self):
        if self._value:
            return self._value.endswith('?')
        return False

    def is_exclamation(self):
        if self._value:
            return self._value.endswith('!')
        return False

    def count_sentences(self):
        if self._value:
            sentences = [sentence.strip() for sentence in re.split(r'[.!?]', self._value) if sentence]
            return len(sentences)
        return 0

# Example usage:
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())       # Output: False
print(string.is_question())       # Output: True
print(string.is_exclamation())    # Output: False
print(string.count_sentences())   # Output: 3




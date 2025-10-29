#!/usr/bin/env python3

def add_suffix(words, suffix):
    # your code here
    # do not forget to pass the correct function parameters
    for i in range(len(words)):
        words[i] = words[i] + suffix

# sample function call
words = ["cat", "dog", "bird"]
print(words)                   # expected output: ['cat', 'dog', 'bird']
add_suffix(words, "_pet")           
print(words)                   # expected output: ['cat_pet', 'dog_pet', 'bird_pet']


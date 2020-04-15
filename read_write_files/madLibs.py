#! python3
# madLibs.py - Program to read text files and prompts users to add their own text from regular expression matches

import re

file = open('.\\madlibs.txt', 'r')
content = file.read()
mad_lib_words = list(content.split())
file.close()

adj_regex = re.compile(r'ADJECTIVE')
noun_regex = re.compile(r'NOUN')
adv_regex = re.compile(r'ADVERB')
verb_regex = re.compile(r'VERB')

result_file = open('.\\madlibsresult.txt', 'w')
result_string = ""
for word in mad_lib_words:
    if adj_regex.match(word):
        word = adj_regex.sub(input('Give an adjective: '), word)
    elif noun_regex.match(word):
        word = noun_regex.sub(input('Give a noun: '), word)
    elif adv_regex.match(word):
        word = adv_regex.sub(input('Give an adverb: '), word)
    elif verb_regex.match(word):
        word = verb_regex.sub(input('Give a verb: '), word)

    result_string += word + ' '
    result_file.write(word + ' ')

print(result_string)
result_file.close()

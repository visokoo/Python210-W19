#!/usr/bin/env python3
'''
----------------------------------------------------
Assignment: trigrams.py
Author: visokoo | Created: 2/2/2019
ChangeLog: 2/2/2019, Created file

"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]
----------------------------------------------------
'''

import random
punc = ["'", ",", "\"", "(", ")", ".", "-"]
test_str = "I wish I may I wish I might".split()

def build_trigrams(str):
  trigrams = {}
  for word in range(len(str) - 2):
    pair = tuple(str[word:word + 2])
    follower = str[word + 2]
    if pair in trigrams:
      trigrams[pair] += [follower]
    else:
      trigrams.update({pair: [follower]})
  return trigrams

def read_file(file):
  list_of_words = []
  with open(file, 'r') as infile:
    scrape = infile.readlines()
    for line in scrape:
      for punctuation in punc:
        line = line.replace(punctuation, " ")
      else:
        l = line.split()
        list_of_words += l
    return list_of_words

def build_new_text(tri):
  start_pair = random.choice(list(tri.keys()))
  word_list = list(start_pair)
  while True:
    if start_pair in tri:
      third_word = random.choice(tri[start_pair])
      word_list.append(third_word)
      # reset start_pair to last two values as key
      start_pair = tuple(word_list[-2:])
    else:
      break
  # cap first word in list
  word_list[0] = word_list[0].capitalize()
  print(" ".join(word_list))

filename = "sherlock_small.txt"
trigrams = build_trigrams(read_file(filename))
build_new_text(trigrams)
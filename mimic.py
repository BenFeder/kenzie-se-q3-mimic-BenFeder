#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Benjamin Feder"


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    with open(filename, "r") as file:

        for line in file:

            words = line.split()[:-1]

            mapped_dict = {}

            mapped_dict[""] = list(words[0])

            for word in words:

                if word not in mapped_dict.keys():

                    next_index = words.index(word) + 1

                    mapped_dict[word] = list(words[next_index])

                else:

                    next_index = words.index(word) + 1

                    mapped_dict[word].extend(list(words[next_index]))

            return mapped_dict

            #     words = line.split()

            #     next_dict = {}

            #     next_dict[""] = list(words[0])

            #     for word in words:

            #         if word != words[-1]:

            #             next_words_indices = []
            #             offset = -1
            #             while True:
            #                 try:
            #                     offset = words.index(word, offset+1)
            #                 except ValueError:
            #                     continue
            #                 next_words_indices.append(offset)

            #             for next_word in next_words_indices:

            #                 next_dict[word] = next_dict[word].append(
            #                 list(words[next_word]))

            # return next_dict


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    output = ""  # set output to empty string

    # add start word to output based on empty string "" as key from dictionary
    output += mimic_dict[""]

    last_word = ""

    # repeat num_words times, getting next word after each subsequent word
    for word in range(num_words):

        # select a random word from the next list, using last_word
        # as the dictionary key
        output += random.choice(mimic_dict[last_word])

        # create list of output words
        output_list = output.split()

        # get last word from output to use as key for
        # next word to add to output
        last_word = output_list[-1]

    # print output
    print(output)


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')

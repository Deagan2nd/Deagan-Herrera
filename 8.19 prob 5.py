#-------------------------------------------------------------------------------
# Name:        8.19 prob 5
# Purpose:
#
# Author:      drherrera
#
# Created:     14/10/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string


Ashborn = """I Am The Record Of Your Struggles, The Evidence Of Your Resistance, And The Reward Of Your Sufferings. I Am Death, I Am Eternal Rest, I Am Terror, I am You."""


def remove_punctuation(text):
    result = ""
    for letter in text:
        if letter not in string.punctuation:
            result += letter
    return result


def count_e_words(word_list):
    count = 0
    for word in word_list:
        if "e" in word or "E" in word:
            count += 1
    return count

clean_text = remove_punctuation(Ashborn)
words = clean_text.split()


total_words = len(words)
e_words = count_e_words(words)
percentage = (e_words / total_words) * 100


print("Your text contains " + str(total_words) + " words, of which " +
      str(e_words) + " (" + str(round(percentage, 1)) + "%) contain an \"e\".")
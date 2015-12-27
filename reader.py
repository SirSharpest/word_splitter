######################################################
# This is a simple program which will read a file of
# new line seperated words and sort them into new files
# based on their length i.e. all 6 letter words into one file
######################################################

from os.path import isfile
import re
file = 'words.txt'

pattern = re.compile("[a-z]+$")

with open(file) as f:
    for line in f:
        word_length = len(line) -1 # Minus 1 because of the \n counting as a character here
        with open(str(word_length) + '.txt.', 'a') as word_file:
            # check that line only contains a-z characters in lowercase
            if pattern.match(line):
                word_file.write(line)
                word_file.close()
            else:
                print('This isn\'t a word: ' + line.strip('\n'))
                continue


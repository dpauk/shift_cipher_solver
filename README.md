# Shift cipher solver

A very stupid shift cipher solver.  For now it just bases the plaintext output on an exact frequency match of the ciphertext to a set of expected frequencies.

The expected_frequencies.txt file is taken from http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/

Todo:

[ ] Allow it to deal with numbers and both upper and lower case characters.

[ ] Create better ways of solving e.g. convert the characters before the first space - if it's not a word, try again.

[ ] Make the process more interactive - allow the plaintext to be updated based on user input of the expected character.

import operator
import os
import re


def open_ciphertext_file(filename):
    try:
        with open(filename, 'r') as ciphertext_file:
            ciphertext = ciphertext_file.read().replace('\n', '')
    except FileNotFoundError:
        raise FileNotFoundError
    return ciphertext


def calculate_character_frequency_in_ciphertext(ciphertext):
    character_frequencies = {}
    for character in ciphertext:
        if ' ' in character:
            continue
        if character in character_frequencies:
            character_frequencies[character] += 1
        else:
            character_frequencies[character] = 1
    return character_frequencies


def open_expected_frequencies_file(filename):
    expected_frequencies = {}

    row_regex = re.compile('[A-Z]\s:\s+\d+.\d+')
    character_regex = '[A-Z]'
    percentage_regex = '\d+[.]\d+'

    try:
        with open(filename, 'r') as expected_frequencies_file:
            for line in expected_frequencies_file:
                if not row_regex.match(line):
                    raise ValueError
                character = re.search(character_regex, line).group(0)
                percentage_frequency = float(re.search(percentage_regex, line).group(0))
                frequency = percentage_frequency / 100
                expected_frequencies[character] = frequency
    except FileNotFoundError:
        raise FileNotFoundError

    return expected_frequencies


def create_ordered_list_by_frequency(frequency_dictionary):
    """Takes a dictionary of letters and frequencies and returns a list
        with the characters by frequency"""
    return sorted(frequency_dictionary.items(), key=operator.itemgetter(1), reverse=True)


def solve_by_exact_match_of_frequencies(ciphertext, ciphertext_in_order, expected_in_order):
    replacements = {}

    current_position_in_character_in_order = 0

    for character in ciphertext_in_order:
        replacements[character[0]] = expected_in_order[current_position_in_character_in_order][0]
        current_position_in_character_in_order += 1

    plaintext = ''

    for character in ciphertext:
        if ' ' in character:
            plaintext += ' '
            continue
        plaintext += replacements[character]

    return plaintext


if __name__ == '__main__':
    cwd = os.getcwd()
    ciphertext_path = os.path.join(cwd, 'ciphertext.txt')
    ciphertext = open_ciphertext_file(ciphertext_path)
    ciphertext_character_frequencies = calculate_character_frequency_in_ciphertext(ciphertext)
    ciphertext_characters_ordered_by_frequency = create_ordered_list_by_frequency(ciphertext_character_frequencies)

    expected_frequencies_path = os.path.join(cwd, 'expected_frequencies.txt')
    expcted_frequencies = open_expected_frequencies_file(expected_frequencies_path)
    
    expected_characters_ordered_by_frequency = create_ordered_list_by_frequency(expcted_frequencies)

    print("\n*** Plaintext based on an exact match of character frequencies ***:\n")
    print(solve_by_exact_match_of_frequencies(ciphertext, ciphertext_characters_ordered_by_frequency, expected_characters_ordered_by_frequency))

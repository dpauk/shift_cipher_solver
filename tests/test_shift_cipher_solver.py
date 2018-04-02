import os

import pytest

from shift_cipher_solver.shift_cipher_solver import open_ciphertext_file,\
                                                    calculate_character_frequency_in_ciphertext,\
                                                    open_expected_frequencies_file,\
                                                    create_ordered_list_by_frequency,\
                                                    solve_by_exact_match_of_frequencies


def test_open_ciphertext_file_file_missing():
    with pytest.raises(FileNotFoundError):
        open_ciphertext_file('i_do_not_exist.txt')


def test_open_ciphertext_file_file_exists():
    cwd = os.getcwd()
    ciphertext_path = os.path.join(cwd, 'ciphertext.txt')
    ciphertext = open_ciphertext_file(ciphertext_path)
    assert len(ciphertext) != 0


def test_calculate_character_frequency_in_ciphertext_correct():
    ciphertext = 'ababca'
    expected_frequencies = {'a': 3, 'b': 2, 'c': 1}
    assert calculate_character_frequency_in_ciphertext(ciphertext) == expected_frequencies


def test_calculate_character_frequency_in_ciphertext_just_space():
    ciphertext = ' '
    expected_frequencies = {'a': 3, 'b': 2, 'c': 1}
    assert len(calculate_character_frequency_in_ciphertext(ciphertext)) == 0


def test_open_expected_frequencies_file_file_missing():
    with pytest.raises(FileNotFoundError):
        open_expected_frequencies_file('i_do_not_exist.txt')


def test_open_expected_frequencies_file_file_contains_invalid_line():
    cwd = os.getcwd()
    invalid_expected_frequencies_path = os.path.join(cwd, 'invalid_expected_frequencies.txt')
    with pytest.raises(ValueError):
        open_expected_frequencies_file(invalid_expected_frequencies_path)


def test_open_expected_frequencies_file_file_exists():
    cwd = os.getcwd()
    expected_frequencies_path = os.path.join(cwd, 'expected_frequencies.txt')
    expcted_frequencies = open_expected_frequencies_file(expected_frequencies_path)
    assert len(expcted_frequencies) != 0
    assert expcted_frequencies['A'] == 0.0855


def test_create_ordered_list_by_frequency():
    dummy_dictionary = {'A': 0.0855, 'B': 0.016, 'C': 0.0316}
    expected_result = [('A', 0.0855), ('C', 0.0316), ('B', 0.016)]
    assert create_ordered_list_by_frequency(dummy_dictionary) == expected_result


def test_solve_by_exact_match_of_frequencies_correct():
    ciphertext = 'xxxyyz'
    ciphertext_by_frequency = [('x', 3), ('y', 2), ('z', 1)]
    expected_by_frequency = [('a', 3), ('b', 2), ('c', 1)]
    expected = 'aaabbc'
    assert solve_by_exact_match_of_frequencies(ciphertext, ciphertext_by_frequency, expected_by_frequency) == expected


def test_solve_by_exact_match_of_frequencies_just_space():
    ciphertext = ' '
    ciphertext_by_frequency = [('a', 1)]
    expected_by_frequency = [('z', 1)]
    expected = ' '
    assert solve_by_exact_match_of_frequencies(ciphertext, ciphertext_by_frequency, expected_by_frequency) == expected

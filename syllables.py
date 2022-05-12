#!/usr/bin/env python3

import os


class SyllablesWriter:
    VOWELS_FILEPATH = 'vowels.txt'
    ALPHABET_FILEPATH = 'alphabet.txt'
    SYLLABLES_DIRPATH = 'syllables'

    @staticmethod
    def line_reader(filename):
        with open(filename) as file_:
            lines = file_.read().splitlines()
        return lines

    def __init__(self):
        self.vowels = self.line_reader(self.VOWELS_FILEPATH)
        self.alphabet = self.line_reader(self.ALPHABET_FILEPATH)

    def main(self):
        try:
            os.makedirs(self.SYLLABLES_DIRPATH)
        except FileExistsError:
            # It is there already
            pass

        for letter in self.alphabet:
            syllable_filepath = f'{self.SYLLABLES_DIRPATH}/{letter}.txt'
            with open(syllable_filepath, 'w') as syllable_file:
                for vowel in self.vowels:
                    syllable = f'{letter}{vowel}'
                    syllable_file.write(f'{syllable}\n')


if __name__ == '__main__':
    SyllablesWriter().main()

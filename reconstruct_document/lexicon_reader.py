#!/usr/bin/python
# Author: Kaunil N. Dhruv <dhruv.kaunil@gmail.com> * <kaunil.dhruv@colorado.edu>

class LexiconReader:
    """
        --  This reads the lexicons from a text file.
        --  It assumes that the lexicons are seperated by a newline '\n'
            character.
        --  After the file has been read, it stores all the lexicons as strings
            in a list data structure.
    """
    def __init__(self, file_path, verbose):
        """
            Initialize a LexiconReader object.

            :param file_path:   path to the file containing lexicons
            :type file_path:    str


            class variables:
            _lexicons:  1D array/list containing lexicons extracted from the
                        file_path
        """
        self._lexicons = []
        self._file_path = file_path
        self._TAG = 'LexiconReader'

        if verbose:
            print('{}: Building vocabulary from the file located at: {}'
                .format(self._TAG, self._file_path)
                )

        try:
            with open(self._file_path, 'r') as file:
                for line in file:
                    self._lexicons.append(line.strip())
            if verbose:
                print('{}: {} lexicons read.'
                    .format(self._TAG, len(self._lexicons))
                    )
        except Exception as ex:
            print('{}: File error: Lexicon file is not found or is curropt.'
                .format(self._TAG)
            )
            exit(1)

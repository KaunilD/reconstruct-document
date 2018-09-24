#!/usr/bin/python
# Author: Kaunil N. Dhruv <dhruv.kaunil@gmail.com> * <kaunil.dhruv@colorado.edu>

class CorpousReader:
    """
        --  This class reads the text from a document.
        --  It assumes that each sentence in the document is seperated by a '.'.
        --  Each line read by this class is then split into two or more sentences
            using the '.' as an anchor.
        --  After seperating individual sentences, it stores them in a list
            data structure.
        For example:
            -- thequick.brownfox.jumpsover.alazydog
                Is split into:
            -- [thequick, brownfox, jumpsover, alazydog]
    """
    def __init__(self, file_path, verbose):
        """
            Initialize a CorpousReader object.

            :param file_path:   path to the file containing '.' seperated runined sentences.
            :type file_path:    str

            class variables:
            _corpous:   1D array/list containing each sentence seperated by a '.'
                        which is read from the file_path.
        """
        self._corpous = []
        self._file_path = file_path
        self._verbose = verbose
        self._TAG = 'CorpousReader'
        print('')
        if self._verbose:
            print('{}: Reading ruined document located at: {}'
                .format(self._TAG, self._file_path)
            )

        try:
            with open(self._file_path, 'r') as file:
                for line in file:
                    #   remove any trailing whitespaces
                    sentences = line.strip()
                    #   split every sentence using a '.'
                    sentences = sentences.split('.')
                    for sentence in sentences[0:-1]:
                        self._corpous.append(sentence)
            if self._verbose:
                print('{}: {} sentences read.'
                .format(self._TAG, len(self._corpous)))
            print('')
        except Exception as ex:
            print('{}: File error: Corpous file is not found or is curropt.'
                .format(self._TAG)
            )
            exit(1)

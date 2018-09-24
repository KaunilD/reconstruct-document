#!/usr/bin/python
# Author: Kaunil N. Dhruv <dhruv.kaunil@gmail.com> * <kaunil.dhruv@colorado.edu>

class FileWriter:
    """
        --  This class simply writes the data to a file.
        --  It assumes that the data to be written is a list containing words
            obtained via the ReconstructDocument class.
    """
    def __init__(self, file_path, verbose):
        """
            Initialize the FileWriter utility.

            :param file_path:   path to the file containing '.' seperated
                                runined sentences.
            :type file_path:    str

            class variables:
            _corpous:   1D array/list containing each sentence seperated by a '.'
                        which is read from the file_path.
        """
        self._verbose = verbose
        self._file_path = file_path
        self._TAG = 'FileWriter'
    def write(self, sentences):
        """
            This method writes the sentences to a file.

            :param sentences:   2D list of words. Each list containing words which
                                form a sentence.
            :type sentences:    str

        """
        try:
            file = open(self._file_path, 'w+')
            for sentence in sentences:
                for idx, word in enumerate(sentence):
                    if idx == len(sentence)-1:
                        file.write(word + '. ')
                    else:
                        file.write(word + ' ')
            file.close()
            if self._verbose:
                print('{}: {} sentences written to file: {}'
                    .format(
                        self._TAG, len(sentences), self._file_path
                    )
                )
        except Exception as ex:
            print('{}: File error: Writing to disk not premitted. \
                    Run as administrator or su.'.format(self._TAG)
                )
            exit(1)

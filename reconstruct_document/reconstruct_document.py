#!/usr/bin/python
# Author: Kaunil N. Dhruv <dhruv.kaunil@gmail.com> * <kaunil.dhruv@colorado.edu>
"""
    Command line document reconstruction utility.

    This module is takes a lexicon and a ruined document as the input, and returns
    the document with it's spaces restored.

    =============
    EXAMPLE USAGE
    =============

    python main.py example-lexicon.txt doc1.txt output.txt

    ==========================================
    ASSUMPTIONS REGARDING THE RUINED DOCUMENT:
    ==========================================
    1   The sentences of a document have been seperated by a '.'.
    2   Documents only contain characters 'a-z' and '.'.
    3   Every document has atleast 1 valid reconstruction.
    4   The sentences are composed of the words mentioned in the lexicon.

    =======
    LEXICON
    =======
    1   A text file of all the words using which the documents mentioned above
        are constructed.
"""


__version__ = '1.0.0'


import sys
import argparse
from .lexicon_reader import LexiconReader
from .corpous_reader import CorpousReader
from .file_writer import FileWriter


class ReconstructDocument:
    """
        --  This class is the main entry point of the command line utility.
        --  Its uses the LexiconReader and CorpousReader to read the lexicons
            and stripped off sentences.
        --  As an output it generates a file containing reconstructed sentences
            with words seperated by spaces.
    """
    def __init__(self, lexicons_file_path, corpous_file_path, output_file_path, verbose = False):
        """

            :param lexicons_file_path:  path to the lexicon file.
            :type lexicons_file_path:   str

            :param corpous_file_path:   path to the ruined documents.
            :type corpous_file_path:    str

            :param output_file_path:    path to the file where the reconstructed
                                        document need to be written.
            :type output_file_path:     str

            class variables:
                _lexicons:          list of all the lexicons read by the LexiconReader.
                _joined_sentences:  list of all  the sentences read from the
                                    ruined document.
                _file_writer:       FileWriter object to write the reconstructed
                                    sentences to a file.
                _reconstructed_sentences:
                                    list of words found in the lexicons extracted
                                    from the ruined document/_joined_sentences.

        """
        self._lexicons = LexiconReader(lexicons_file_path, verbose)._lexicons
        self._joined_sentences = CorpousReader(corpous_file_path, verbose)._corpous
        self._file_writer = FileWriter(output_file_path, verbose)
        self._reconstructed_sentences = []
        self._TAG = 'ReconstructDocument'

    def reconstruct(self):
        """
            This method does the actual reconstruction of sentences.
        """
        for idx, sentence in enumerate(self._joined_sentences):
            # array of booleans to represent if the sequence is a valid word from
            # a dictionary of lexicons.
            segmented = [True]
            self._reconstructed_sentences.append([])
            for i in range (0, len(sentence)):
                # new word started, mark it as the begining.
                segmented.append(False)
                for j in range(i,-1,-1):
                    # if the last detected substring from this position is valid
                    # and the next character  is valid as well then join them to
                    # form a complete string from  the dictionary.
                    if segmented[j] and sentence[j:i+1] in self._lexicons:
                        segmented[i+1] = True
                        # if the last appended word is a substring of the lexicon
                        # from the dictionary then replace the last word with
                        # complete word from the dictionary. Else, simply append
                        # the current substring.
                        if len(self._reconstructed_sentences[-1]) > 0 and \
                            self._reconstructed_sentences[-1][-1] in sentence[j:i+1]:
                            self._reconstructed_sentences[-1][-1] = sentence[j:i+1]
                        else:
                            self._reconstructed_sentences[-1].append(sentence[j:i+1])
                        break
        self.write_to_file()

    def write_to_file(self):
        """
            A silly wrapper for writing the reconstructed sentences to file.
        """
        self._file_writer.write(self._reconstructed_sentences)


def create_args():
    parser = argparse.ArgumentParser(
            description='RECONSTRUCT RUINED DOCUMENTS. This command line utility\
                will allow you to recover a document which is stripped off all the\
                whitespaces with the help of a "--lexicon" - a dictionary of valid words\
                to be used. The recovered document will be written to a file\
                specified using the argument - "--document".'
        )
    parser.add_argument('lexicon', type=str,
                            help='File path containing a dictionary of words \
                            to be used to re-construct the document.'
                        )
    parser.add_argument('document', type=str,
                            help='File path to the ruined document.'
                        )
    parser.add_argument('output', type=str,
                            help='File path to which the reconstructed document will\
                            be written'
                        )
    parser.add_argument('-v', '--verbose', type=str,
                            default=True,
                            help='Tell\'s you all the silly and minute details.'
                        )
    return parser.parse_args()


def main():
    args = create_args()

    documentReconstructor = ReconstructDocument(
        args.lexicon,
        args.document,
        args.output,
        args.verbose
    )

    documentReconstructor.reconstruct()

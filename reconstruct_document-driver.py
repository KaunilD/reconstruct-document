#!/usr/bin/env python
# Author: Kaunil N. Dhruv <dhruv.kaunil@gmail.com> * <kaunil.dhruv@colorado.edu>

"""
    Convienence wrapper for running reconstruct_document directly from the source
    tree.

    =============
    EXAMPLE USAGE
    =============

    python reconstruct_document-driver.py example-lexicon.txt doc1.txt output.txt

"""

from reconstruct_document.reconstruct_document import main

if __name__ == '__main__':
    main()

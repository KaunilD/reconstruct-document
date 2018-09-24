# Reconstruct Document [reconstruct_document]

Command line document reconstruction utility.

__reconstruct_document__ takes a _lexicon_ and a _ruined document_ as input, and writes the prettified version of the runined document by restoring the spaces to the disk.

### Features
 - A commandline utility.
 - Install once use anywhere.
 - Supported with Ubuntu, Mac and a limited support on Windows.
 - Built with python.

### Dependencies
 1. python 3.X
 2. Reconstruct Document uses packages included in standard distributions of python such as:
    1. os
    2. argparse
    3. sys
    4. setuptools (for installation)


### Installation

Install using [python](https://www.python.org/downloads/release/python-370/)

```sh
$ cd reconstruct-document
$ python setup.py install
```

### Usage

- This modules requires 3 positional arguments to run.
    1. lexicon file
    2. runined document
    3. output file path

- You can also ask it __not__ to be verbose by supplying the optional argument `-v False` or `--verbose False`.

##### Example [without install]
* You can use this utility without any installation by executing the driver script -   `reconstruct_document-driver.py` located in the root of `reconstruct-docuemnt/`.

* For Example:
    ```bash
    $ python reconstruct_document-driver.py data/example-lexicon.txt data/ruined-documents/doc1.txt data/output.txt
    ````

##### Example [with install]

* __After__ you are happy with the utility and have __installed__ it using the installation steps mentioned above, you can __execute the utility system-wide__ using the following command:
    ```bash
    $ reconstruct_document data/example-lexicon.txt data/ruined-documents/doc1.txt data/output.txt
    ```

#### Testing
-   You can execute unittests on all the compoenets of this module using the following command in the      utility root:

    ```bash
      $ python -m unittest discover -v
    ```

#### NOTE:    
-   Assumptions regarding the ruined document
    1.   The sentences of a document have been seperated by a '.'.
    2.   Documents only contain characters 'a-z' and '.'.
    3.  Every document has atleast 1 valid reconstruction.
    4.   The sentences are composed of the words mentioned in the lexicon.

### Todos

 - Provide suport for all the lexicons available in the English vocabulary
 - Include support for grammer such as ',"-'

License
----

MIT

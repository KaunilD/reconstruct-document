import unittest
import os.path
from  reconstruct_document import file_writer


class Test(unittest.TestCase):

    def setUp(self):
        self._output = 'data/out.txt'


    def test_1(self):
        """
            Test FileWriter. If it is not allowed to write a file
            then exit code should be 1.
        """
        _file_writer = file_writer.FileWriter(self._output, False)
        _file_writer.write([''])
        self.assertEqual(os.path.isfile(self._output), True)
if __name__ == '__main__':
    unittest.main()

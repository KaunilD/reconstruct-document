import unittest
from  reconstruct_document import reconstruct_document


class Test(unittest.TestCase):

    def setUp(self):
        self._joined_sentences = [
            'loremipsumdolorsitametconsecteturadipiscingelitseddoeiusmodtemporincididuntutlaboreetdoloremagnaaliqua',
            'utenimadminimveniamquisnostrudexercitationullamcolaborisnisiutaliquipexeacommodoconsequat'
        ]
        self._lexicons = [
            'ad', 'irure', 'in', 'ea', 'excepteur', 'sunt', 'elit', 'duis',
            'sed', 'eiusmod', 'enim', 'eu', 'et', 'labore', 'incididunt',
            'reprehenderit', 'est', 'quis', 'sit', 'deserunt', 'nostrud',
            'qui', 'id', 'consectetur', 'aute', 'dolore', 'mollit', 'aliquip',
            'nulla', 'laborum', 'do', 'non', 'commodo', 'aliqua', 'cillum',
            'sint', 'velit', 'officia', 'veniam', 'consequat', 'magna',
            'cupidatat', 'ullamco', 'lorem', 'amet', 'ipsum', 'nisi', 'fugiat',
            'occaecat', 'proident', 'ut', 'minim', 'culpa', 'tempor', 'pariatur',
            'laboris', 'anim', 'adipiscing', 'dolor', 'voluptate', 'esse',
            'exercitation', 'ex'
        ]
        self._reconstructed_sentences = [
            [
                'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing',
                'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut',
                'labore', 'et', 'dolore', 'lorem', 'magna', 'aliqua'
            ],
            [
                'ut', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud', 'exercitation',
                'ullamco', 'laboris', 'nisi', 'ut', 'aliquip', 'ex', 'ea', 'commodo',
                'consequat'
            ]
        ]
        self.lexicon_file_path = 'data/example-lexicon.txt'
        self.document = 'data/ruined-documents/doc1.txt'
        self.output = 'data/out.txt'
        self.func = reconstruct_document.ReconstructDocument(
            self.lexicon_file_path,
            self.document,
            self.output
        )

    def test_1(self):
        """
            Test if LexiconReader is functioning
        """
        self.assertEqual(self.func._lexicons, self._lexicons)

    def test_2(self):
        """
            Test for CorpousReader
        """
        self.assertEqual(self.func._joined_sentences, self._joined_sentences)

    def test_3(self):
        """
            Test ReconstructDocument
        """
        self.func.reconstruct()
        self.assertEqual(self.func._reconstructed_sentences, self._reconstructed_sentences)
if __name__ == '__main__':
    unittest.main()

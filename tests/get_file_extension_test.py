from unittest import TestCase, main

from regex_tools import get_file_extension


class FileExtension(TestCase):
    def test_get_file_extension(self):
        self.assertIsInstance(get_file_extension('2023-02-28_20-23-08_report.pdf'), str)

        self.assertEqual(get_file_extension('2023-02-28_20-23-08_report.pdf'), 'pdf')

        self.assertEqual(get_file_extension('.DS_store'), 'DS_store')

        self.assertEqual(get_file_extension('20231006EPAV2441.ORF.dop'), 'dop')


if __name__ == '__main__':
    main()

from unittest import TestCase, main

from find_file_hdd import find_files_in_dir_with_extension


class FindFilesInDirectory(TestCase):
    def test_find_files_in_dir_with_extension(self):
        tested_function = find_files_in_dir_with_extension('../tests/test_files',
                                                           files_extensions=('jpg', 'jpeg', 'dng', 'nef', 'orf'))
        self.assertIsInstance(tested_function,
                              list)

        self.assertEqual(tested_function[0],
                         '../tests/test_files/KSP_018082_00016_1h.JPG', )


if __name__ == '__main__':
    main()

from unittest import TestCase, main

from metadata_tools.read_metadata_from_image import read_image_metadate

TEST_JPEG = '../tests/test_files/KSP_018082_00016_1h.JPG'


class ReadImageMetadata(TestCase):
    def test_read_image_metadate(self):
        self.assertIsInstance(read_image_metadate(TEST_JPEG), dict)
        self.assertEqual(read_image_metadate(TEST_JPEG)['File:Directory'], '../tests/test_files')


if __name__ == '__main__':
    main()

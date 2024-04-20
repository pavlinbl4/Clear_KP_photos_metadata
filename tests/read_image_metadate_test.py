from unittest import TestCase, main

from metadata_tools.read_metadata import read_image_metadate

TEST_JPEG = '../tests/test_files/20231214EPAV9435.jpg'
# '../tests/test_files/KSP_015561_00123_1h.jpg'


class ReadImageMetadata(TestCase):
    def test_read_image_metadate(self):
        self.assertIsInstance(read_image_metadate(TEST_JPEG), dict)
        self.assertEqual(read_image_metadate(TEST_JPEG)['Composite:LensID'], 'OLYMPUS M.7-14mm F2.8')


if __name__ == '__main__':
    main()

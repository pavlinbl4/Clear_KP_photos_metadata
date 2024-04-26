# get all image metadata from file
import exiftool
from icecream import ic


def read_image_metadate(path_to_image_file: str) -> dict:
    with exiftool.ExifToolHelper() as et:
        image_metadate = et.get_metadata(path_to_image_file)[0]
        return image_metadate


if __name__ == '__main__':
    ic(read_image_metadate('../tests/test_files/KSP_018082_00016_1h.JPG'))

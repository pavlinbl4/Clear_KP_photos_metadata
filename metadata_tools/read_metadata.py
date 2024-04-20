# get all image metadata from file
import exiftool
from icecream import ic
from loguru import logger


def read_image_metadate(path_to_image_file):
    with exiftool.ExifToolHelper() as et:
        image_metadate = et.get_metadata(path_to_image_file)[0]
        # logger.info()
        return image_metadate


def read_tag(path_to_image_file):
    with exiftool.ExifToolHelper() as et:
        return et.get_tags(path_to_image_file, ['XMP:Model', 'XMP:Description'])


if __name__ == '__main__':
    image = '../tests/test_files/KSP_015561_00123_1h.jpg'
    image2 = '../tests/test_files/20231214EPAV9435.jpg'
    image3 = '../tests/test_files/20211201PEV_2795-Edit.JPG'
    ic(read_image_metadate(image2
        ))
    # print(read_tag('/Volumes/big4photo-4/KP_yellow/KSP_013422_00453_1h.jpg')[0].setdefault(
    #     'XMP:Description', 'NO CAPTION'))

import exiftool
from icecream import ic

from metadata_tools.read_metadata_from_image import read_image_metadate


def clear_all_metadate(path_to_image_file):
    with exiftool.ExifTool() as et:
        # Remove all metadata from an image
        et.execute("-all=", path_to_image_file)


if __name__ == '__main__':
    image3 = '../tests/test_files/20211201PEV_2795-Edit.JPG'
    # ic(read_image_metadate(image3
    #     ))
    clear_all_metadate(image3)
    ic(read_image_metadate(image3
                           ))

# read metadate from image and save it to pickle file
from icecream import ic

from metadata_tools.clear_image_metadate import clear_all_metadate
from metadata_tools.read_metadata_from_image import save_metadate_in_pickle_file, read_image_metadate
from metadata_tools.read_metadate_from_csv_file import read_important_metadate_from_pickle_file
from metadata_tools.unwanted_tags import clear_unwanted_tags
from metadata_tools.write_metadata import add_xmp_date_to_image_file
from regex_tools import modify_caption


def metadate_clearing(path_to_image_file):
    # read_image_metadate(path_to_image_file)
    path_to_pickle_file = save_metadate_in_pickle_file(path_to_image_file)

    # clear all metadate in image
    clear_all_metadate(path_to_image_file)

    # read only important date from pickle file
    xmp_date_dict = read_important_metadate_from_pickle_file(path_to_pickle_file)

    # modify caption
    updated_metadata = modify_caption(xmp_date_dict)

    # clear unwanted tags
    updated_metadata = clear_unwanted_tags(updated_metadata)

    # write this date to image
    add_xmp_date_to_image_file(path_to_image_file, updated_metadata)

    ic(read_image_metadate(path_to_image_file))


if __name__ == '__main__':
    image2 = '/Volumes/big4photo/_PYTHON/Clear_KP_photos_metadata/tests/test_files/20211201PEV_2795-Edit.JPG'
    metadate_clearing(image2)

# read metadata from image and save it to pickle file
from file_permission import change_file_permissions
from metadata_tools.clear_image_metadate import clear_all_metadate

from metadata_tools.unwanted_tags import clear_unwanted_tags
from metadata_tools.write_metadata import add_xmp_date_to_image_file
from pickle_files.work_with_pickle import save_metadate_in_pickle_file, read_important_metadate_from_pickle_file
from regex_tools import modify_caption


def metadate_clearing(path_to_image_file):
    # read_image_metadate(path_to_image_file)
    path_to_pickle_file = save_metadate_in_pickle_file(path_to_image_file)

    # change file permission
    change_file_permissions(path_to_image_file, 0o777)

    # clear all metadata in image
    clear_all_metadate(path_to_image_file)

    # read only important date from pickle file
    xmp_date_dict = read_important_metadate_from_pickle_file(path_to_pickle_file)

    # modify caption
    updated_metadata = modify_caption(xmp_date_dict)

    # clear unwanted tags
    updated_metadata = clear_unwanted_tags(updated_metadata)

    # write this date to image
    add_xmp_date_to_image_file(path_to_image_file, updated_metadata)

    # ic(read_image_metadate(path_to_image_file))

if __name__ == '__main__':
    metadate_clearing('/Volumes/big4photo-4/selenium_downloads/keyword__KSP_016778/KSP_016778_00200_1h.jpg')

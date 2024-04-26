from metadata_tools.read_metadata_from_image import read_image_metadate
from metadata_tools.write_metadata import write_edited_tags
from regex_tools import modify_caption
from icecream import ic


def clear_image_metadata_from_kp_info(path_to_image_file: str):
    # read metadata
    image_metadata: dict = read_image_metadate(path_to_image_file)
    # ic(image_metadata)

    # modify caption
    updated_metadata: dict = modify_caption(image_metadata)
    # ic(updated_metadata)

    # save updates metadata to file
    write_edited_tags(updated_metadata)

if __name__ == '__main__':
    clear_image_metadata_from_kp_info('/Volumes/big4photo-4/KP_yellow/KSP_013422_00453_1h.jpg')
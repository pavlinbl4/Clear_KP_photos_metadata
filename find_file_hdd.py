import os

from metadata_tools.clear_from_kp import clear_image_metadata_from_kp_info
from regex_tools import get_file_extension, get_file_name_no_extension
from loguru import logger


def find_no_ext(file_name_no_extension: str, path: str):  # this will match a file_name
    result = []
    for root, dirs, files in os.walk(path):
        for file in [elem for elem in files if elem.split('.')[-1].lower() in ('dng', 'nef', 'orf', 'jpg', 'jpeg')]:
            if get_file_name_no_extension(file) == file_name_no_extension:
                result.append(os.path.join(root, file))
    return result  # возвращает список с путем к оригинальному файлу


# function to find all images and send them to function
def action_with_image_files_in_directory(path: str, function_to_work_with_files):
    for root, dirs, files in os.walk(path):
        for file in files:
            if get_file_extension(file).lower() in ('jpg', 'jpeg', 'ORF', 'DNG', 'dng', 'NEF', 'nef', 'orf'):
                # you can add any function to work with file
                logger.info(f"{root}/{file}")
                clear_image_metadata_from_kp_info(f"{root}/{file}")

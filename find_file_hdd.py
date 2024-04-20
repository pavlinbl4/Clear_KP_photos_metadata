import os
from regex_tools import get_file_extension
from loguru import logger


# function to find all images and send them to function
def find_files_in_dir_with_extension(path: str, files_extensions):
    list_of_files_in_dir = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if get_file_extension(file).lower() in files_extensions:
                logger.info(f"{root}/{file}")
                list_of_files_in_dir.append(f"{root}/{file}")
    return list_of_files_in_dir

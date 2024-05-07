import os
import sys

from metadata_tools.metadate_optimization import metadate_clearing
from tk_tools import select_folder_via_gui
from find_file_hdd import find_files_in_dir_with_extension
from loguru import logger

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
log_file_path = os.path.join(script_dir, "metadata_edit.log")

logger.add(log_file_path, format="{time} {level} {message}", level="INFO")
logger.add(log_file_path, format="{time} {level} {message}", level="ERROR")


def main():
    # select directory
    initial_dir = '/Volumes/big4photo-4/KP_yellow'
    path_to_folder = select_folder_via_gui(initial_dir)

    # find all files in directory and subdirectories
    images_list = find_files_in_dir_with_extension(path_to_folder,
                                                   files_extensions=('jpg', 'jpeg', 'dng', 'nef', 'orf'))

    # edit metadata in images
    for image in images_list:
        metadate_clearing(image)


if __name__ == '__main__':
    main()

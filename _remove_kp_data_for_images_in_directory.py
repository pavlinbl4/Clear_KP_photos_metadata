from metadata_tools.metadate_optimization import metadate_clearing
from tk_tools import select_folder_via_gui
from find_file_hdd import find_files_in_dir_with_extension
from loguru import logger

logger.add("output.log", format="{time} {level} {message}", level="ERROR")
logger.add("output.log", format="{time} {level} {message}", level="INFO")


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

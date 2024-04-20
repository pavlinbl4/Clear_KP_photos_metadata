from metadata_tools.clear_from_kp import clear_image_metadata_from_kp_info
from tk_tools import select_folder_via_gui
from find_file_hdd import action_with_image_files_in_directory
from loguru import logger



logger.add("output.log", format="{time} {level} {message}", level="ERROR")
logger.add("output.log", format="{time} {level} {message}", level="INFO")


def main():
    # select directory
    initial_dir = '/Volumes/big4photo-4/KP_yellow'
    path_to_folder = select_folder_via_gui(initial_dir)

    action_with_image_files_in_directory(path_to_folder, clear_image_metadata_from_kp_info)


if __name__ == '__main__':
    main()

import exiftool
from exiftool.exceptions import ExifToolExecuteError
from loguru import logger


def add_xmp_date_to_image_file(path_to_file, xmp_date_dict):
    try:
        with exiftool.ExifToolHelper() as et:
            et.set_tags(path_to_file,
                        xmp_date_dict,
                        # params=["-P", "-overwrite_original"]
                        params=["-m", "-overwrite_original"]

                        )
    except ExifToolExecuteError as e:
        logger.info(f'{e}')



if __name__ == '__main__':
    add_xmp_date_to_image_file('/Volumes/big4photo-4/to_trash',
                               {'XMP:Label': "Green"})


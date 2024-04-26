import exiftool
from exiftool.exceptions import ExifToolExecuteError
from loguru import logger


def write_edited_tags(xmp_tags):
    try:
        with exiftool.ExifToolHelper() as et:
            et.set_tags({xmp_tags['SourceFile']},
                        tags={'XMP:Rights': 'Pavlenko Evgeniy',
                              'XMP:Credit': 'Pavlenko Evgeniy',
                              'XMP:Creator': 'Pavlenko Evgeniy',
                              'XMP:Title': '',
                              'XMP:Label': "Green",
                              'XMP:Description': xmp_tags['XMP:Description'],
                              'IPTC:By-line': 'Pavlenko Evgeniy',
                              'IPTC:Credit': 'Pavlenko Evgeniy',
                              'IPTC:CopyrightNotice': 'Pavlenko Evgeniy',
                              'IPTC:Caption-Abstract': xmp_tags['XMP:Description'],
                              'IPTC:ObjectName': '',
                              'Photoshop:SlicesGroupName': ''
                              },
                        params=["-P", "-overwrite_original"])
    except ExifToolExecuteError as e:
        logger.info(f'{e}\n{xmp_tags}')


def add_xmp_date_to_image_file(path_to_file, xmp_date_dict):
    try:
        with exiftool.ExifToolHelper() as et:
            et.set_tags(path_to_file,
                        xmp_date_dict,
                        params=["-P", "-overwrite_original"])
    except ExifToolExecuteError as e:
        logger.info(f'{e}')

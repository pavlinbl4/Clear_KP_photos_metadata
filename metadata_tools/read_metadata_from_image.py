# get all image metadata from file
import exiftool


def read_image_metadate(path_to_image_file: str) -> dict:
    with exiftool.ExifToolHelper() as et:
        image_metadate = et.get_metadata(path_to_image_file)[0]
        return image_metadate

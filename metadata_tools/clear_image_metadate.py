import exiftool


def clear_all_metadate(path_to_image_file):
    with exiftool.ExifTool() as et:
        # Remove all metadata from an image
        et.execute("-all=", path_to_image_file)

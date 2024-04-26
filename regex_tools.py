import re
from loguru import logger


def get_file_extension(path_to_file: str) -> str:
    re_pattern = r'(?<=\.)[^.]+$'
    extension = re.findall(re_pattern, path_to_file)[0]
    return extension


def modify_caption(image_metadata: dict) -> dict:
    try:
        caption = image_metadata['XMP:Description'].replace('\n', ' ')
        logger.info(caption)

        pattern = r'(?<=RU ).+(?= Фото:)'
        if len(re.findall(pattern, caption)) != 0:
            image_metadata['XMP:Description'] = re.findall(pattern, caption)[0]
    except KeyError as e:
        image_metadata.setdefault('XMP:Description', 'NO CAPTION')
        # print(f"no caption in {e}")
        logger.info(f"no caption in {e}")

    return image_metadata

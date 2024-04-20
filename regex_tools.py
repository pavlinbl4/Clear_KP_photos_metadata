import re
from loguru import logger


def get_file_extension(path_to_file: str) -> str:
    # re_pattern = r'(?<=\.)[1A-Za-z_]{3,8}'  # work correctly with only one dot in filename
    re_pattern = r'(?<=\.)[^.]+$'
    extension = re.findall(re_pattern, path_to_file)[0]
    return extension  # string with file extension


def get_file_name_no_extension(file_name: str):
    rg_pattern = r'[^.]+(?=\.)'
    # didn't work with hidden files
    file_name_no_extension = re.findall(rg_pattern, file_name)
    if len(file_name_no_extension) != 0:
        return file_name_no_extension[0]


def modify_caption(image_metadata):
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


def full_shoot_html_link(shoot_id: str, page: int) -> str:
    # create full shoot html link with 200 preview (Так называемый "просмотр съемки")
    splited_soot_id = shoot_id.split('_')
    return f'https://image.kommersant.ru/photo/wp/default.aspx?shootnum={splited_soot_id[1]}' \
           f'&sourcecode={splited_soot_id[0]}&pagesize=200&previewsize=128&page={str(page)}&nl=true&ord=F'


if __name__ == '__main__':
    assert type(full_shoot_html_link('KSP_017605', 0)) == str
    # print(f"{'replace_to_comma'}: {replace_to_comma('Санкт - Петербург, Петрикирхе;архитектура;религия,религия ')}")
    # print(
    #     f"{'keywords_opimization'}: "
    #     f"{keywords_opimization('Санкт-Петербург, Петрикирхе;архитектура;религия, архитектура')}")
    #
    # print(full_shoot_html_link('KSP_017945', 1))

    assert type(get_file_name_no_extension('KSP_017547_00011_1h.jpg')) == str
    assert len(get_file_name_no_extension('KSP_017547_00011_1h.jpg')) != 0
    assert get_file_name_no_extension('.DS_store') is None
    assert get_file_name_no_extension('KSP_017547_00011_1h.jpg') == 'KSP_017547_00011_1h'
    assert get_file_extension('2023-02-28_20-23-08_report.pdf') == 'pdf'
    assert get_file_extension('.DS_store') == 'DS_store'
    assert get_file_extension('20231006EPAV2441.ORF.dop') == 'dop'

from icecream import ic

from date.tags_to_update import tags
from metadata_tools.read_metadate_from_csv_file import read_important_metadate_from_pickle_file


def clear_unwanted_tags(xmp_date_dict: dict) -> dict:
    xmp_date_dict.update(tags)
    return xmp_date_dict


if __name__ == '__main__':
    xmp_date = read_important_metadate_from_pickle_file('../metadate.pickle')
    ic(xmp_date)
    ic(clear_unwanted_tags(xmp_date))

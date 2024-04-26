from date.tags_to_update import tags


def clear_unwanted_tags(xmp_date_dict: dict) -> dict:
    xmp_date_dict.update(tags)
    return xmp_date_dict

import pickle

from metadata_tools.read_metadata_from_image import read_image_metadate
from metadata_tools.read_metadate_from_file import important_data


def save_metadate_in_pickle_file(path_to_image_file: str):
    metadate_dict = read_image_metadate(path_to_image_file)
    path_to_pickle_file = '../metadate.pickle'
    with open(path_to_pickle_file, 'wb') as pickle_file:
        pickle.dump(metadate_dict, pickle_file)
    return path_to_pickle_file


def read_important_metadate_from_pickle_file(path_to_pickle_file):
    xmp_date_dict = {}
    with open(path_to_pickle_file, 'rb') as pickle_file:
        pickle_dict = pickle.load(pickle_file)
    for key in pickle_dict:
        if key in important_data:
            xmp_date_dict[key] = pickle_dict[key]
    return xmp_date_dict

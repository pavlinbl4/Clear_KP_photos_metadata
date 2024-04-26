"""
function will read only information for good caption of image from csv file
"""

import csv
import pickle

from icecream import ic

important_data = [
    # 'IPTC:Country-PrimaryLocationCode',
    # 'IPTC:By-line',
    # 'IPTC:Caption-Abstract',
    # 'IPTC:CopyrightNotice',
    'XMP:Headline',
    'XMP:Description',
    'XMP:Subject',
    'XMP:Country',
    'XMP:Label',
    'XMP:Rating',
    'XMP:Urgency',
    'XMP:Credit',
    'XMP:Country',
    'XMP:City',
    'XMP:Subject',
    'XMP:Instructions']


def read_important_metadate_from_csv_file(csv_file_with_xmp):
    with open(csv_file_with_xmp, 'r') as csv_file:
        xmp_date_dict = {}
        for line in csv_file:
            # print(line.strip().split(','))
            if line.strip().split(',')[0] in important_data:
                print(line.strip())
                # xmp_date_dict[line.strip().split(',')[0]] = ','.join(line.strip().split(',')[1:])
                xmp_date_dict[line.strip().split(',')[0]] = line.strip().split(',')[1]
        return xmp_date_dict


def read_important_metadate_from_pickle_file(path_to_pickle_file):
    xmp_date_dict = {}
    with open(path_to_pickle_file, 'rb') as pickle_file:
        pickle_dict = pickle.load(pickle_file)
    for key in pickle_dict:
        if key in important_data:
            xmp_date_dict[key] = pickle_dict[key]
    return xmp_date_dict

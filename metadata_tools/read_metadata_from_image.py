# get all image metadata from file
import exiftool
from icecream import ic
from loguru import logger
import csv
import pickle


def read_image_metadate(path_to_image_file: str) -> dict:
    with exiftool.ExifToolHelper() as et:
        image_metadate = et.get_metadata(path_to_image_file)[0]
        return image_metadate


def read_tag(path_to_image_file):
    with exiftool.ExifToolHelper() as et:
        return et.get_tags(path_to_image_file, ['XMP:Model', 'XMP:Description'])


# function to read metadate from image and save it to csv file
def save_metadate_in_file(path_to_image_file: str):
    metadate_dict = read_image_metadate(path_to_image_file)
    with open(f'{metadate_dict["File:FileName"]}_metadate.csv', 'w', newline='') as csv_file:
        cvs_writer = csv.writer(csv_file)
        for key, value in metadate_dict.items():
            print(key, value)
            cvs_writer.writerow([key, value])


def save_metadate_in_pickle_file(path_to_image_file: str):
    metadate_dict = read_image_metadate(path_to_image_file)
    path_to_pickle_file = '../metadate.pickle'
    with open(path_to_pickle_file, 'wb') as pickle_file:
        pickle.dump(metadate_dict, pickle_file)
    return path_to_pickle_file


if __name__ == '__main__':
    image = '../tests/test_files/20211201PEV_2795-Edit.JPG'
    image2 = '../tests/test_files/all_fields.JPG'
    image3 = '../tests/test_files/20211201PEV_2795-Edit.JPG'
    all_fields = '../tests/test_files/all_fields.JPG'
    read_image_metadate(image2)
    # save_metadate_in_file(all_fields)
    # save_metadate_in_pickle_file(image3)

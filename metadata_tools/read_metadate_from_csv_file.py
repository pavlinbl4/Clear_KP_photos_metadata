"""
function will read only information for good caption of image from csv file
"""

import csv
from icecream import ic

from metadata_tools.write_metadata import add_xmp_date_to_image_file


def read_important_metadate_from_csv_file(csv_file_with_xmp):
    with open(csv_file_with_xmp, 'r') as csv_file:
        xmp_date_dict = {}
        important_data = ['IPTC:Country-PrimaryLocationCode',
                          'IPTC:By-line',
                          'IPTC:Caption-Abstract',
                          'IPTC:CopyrightNotice',
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
        for line in csv_file:
            # print(line.strip().split(','))
            if line.strip().split(',')[0] in important_data:
                print(line.strip())
                # xmp_date_dict[line.strip().split(',')[0]] = ','.join(line.strip().split(',')[1:])
                xmp_date_dict[line.strip().split(',')[0]] = line.strip().split(',')[1]
        return xmp_date_dict

if __name__ == '__main__':
    xmp_date = read_important_metadate_from_csv_file('../metadata_tools/all_fields.JPG_metadate.csv')
    ic(xmp_date)

    # add_xmp_date_to_image_file('/Volumes/big4photo/_PYTHON/Clear_KP_photos_metadata/tests/test_files/20211201PEV_2795-Edit.JPG',
    #                            xmp_date)

"""
function will read only information for good caption of image from csv file
"""

import csv
from icecream import ic


with open('../metadata_tools/pavlovsk.JPEG_metadate.csv', 'r')  as csv_file:
    caption_dictionary = {}
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
            # print(line.strip())
            caption_dictionary[line.strip().split(',')[0]] = line.strip().split(',')[1]







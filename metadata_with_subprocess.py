import subprocess
import json
from icecream import ic


def read_exif_data(image_path):
    result = subprocess.run(["exiftool", "-j", image_path], capture_output=True, text=True, check=True)
    metadata = result.stdout.strip()

    return json.loads(metadata)[0]


# Пример использования
image_path = "/Volumes/big4photo-4/to_trash/20200719EPAV0078.DNG"
metadata = read_exif_data(image_path)

if metadata:
    print(metadata['Subject'])
    # ic(metadata)

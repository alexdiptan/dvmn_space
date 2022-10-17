from pathlib import Path

import requests
from dotenv import load_dotenv

import common_functions as com_func


def fetch_epic_images(url: str, payload: dict) -> list:
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_images = []

    for image in response.json():
        current_image_date = com_func.date_normalize(image["identifier"])
        epic_images.append(f'https://api.nasa.gov/EPIC/archive/natural/{current_image_date.year}/'
                           f'{current_image_date.month}/{current_image_date.day}/png/'
                           f'{image["image"]}.png')

    return epic_images


def main():
    load_dotenv()
    image_folder = 'images'
    Path(image_folder).mkdir(parents=True, exist_ok=True)
    url_params = {'api_key': 'DEMO_KEY'}

    epic_image_urls = fetch_epic_images('https://api.nasa.gov/EPIC/api/natural', url_params)
    for epic_image_url in epic_image_urls:
        com_func.save_image(epic_image_url, image_folder, url_params)


if __name__ == '__main__':
    main()

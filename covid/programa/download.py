
import config

import datetime

import requests

import pandas

def get_and_store_web_file(url, date=None):

    if date is None:
        date = datetime.datetime.now().date()

    base_name = url.split('/')[-1]
    base_name = f'{date.year}-{date.month}-{date.day}-{base_name}'
    store_path = config.CACHE_DIR / base_name

    if store_path.exists():
        return store_path

    response = requests.get(url)

    if response.status_code == 404:
        raise RuntimeError(f'Error downloading file: {url}')

    with store_path.open('wb') as fhand:
        for chunk in response.iter_content(chunk_size=128):
            fhand.write(chunk)

    return store_path


def get_isciii_dframe():
    file_csv_path = get_and_store_web_file(config.URL_DATOS_ISCIII)
    covid_df = pandas.read_csv(file_csv_path,
                               parse_dates=[config.ORIG_DATE_COL])
    return covid_df


if __name__ == '__main__':
    print(get_isciii_dframe())

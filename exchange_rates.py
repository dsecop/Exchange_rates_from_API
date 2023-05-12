import csv
from pathlib import Path
import requests
import datetime

from requests import Response

data_dir = (Path.home() / 'currency_data')
data_dir.mkdir(exist_ok=True)

url = 'http://api.exchangeratesapi.io/v1/'
endpoint = 'latest'
payload = {
    'access_key': 'Place your token here',
    'base': 'EUR',
    'symbols': 'PLN, USD, GBP'
}


def connect_to_api_url() -> Response:
    try:
        return requests.get(url + endpoint, params=payload)
    except requests.exceptions.HTTPError as http_err:
        raise SystemExit(http_err)


def get_currency_data() -> dict:
    currency = connect_to_api_url()
    return currency.json()['rates']


def datetime_format() -> str:
    current_date = datetime.datetime.now()
    return str(current_date.strftime('%d_%b_%Y_%H_%M_'))


def save_to_csv() -> None:
    with open(f'{data_dir}/{datetime_format()}currency_rates.csv', mode='w') as csv_f:
        fieldnames = ['PLN', 'USD', 'GBP']
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerow(get_currency_data())


def del_oldest_file() -> None:
    count = 0
    for file in data_dir.iterdir():
        count += 1
        if file.is_file() and count > 7:
            oldest = min([file for file in data_dir.resolve().glob('*.csv')], key=Path)
            oldest.unlink()


def main():
    save_to_csv()
    del_oldest_file()


if __name__ == '__main__':
    main()

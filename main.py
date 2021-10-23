import requests
import json
import datetime as dt
from pathlib import Path
import time


def format_dt(dt):
    return dt.strftime("%Y-%m-%d")


config = json.load(open('./config.json'))


def create_logs(folder, origin, destination):
    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/DK/EUR/en-US/{origin}/{destination}"
    date = dt.datetime(2022, 1, 1)
    today = dt.datetime.now()
    headers = config['headers']

    res_obj = {}
    for i in range(30):
        res = requests.request(
            "GET", f'{url}/{format_dt(date)}', headers=headers).text
        res_obj[format_dt(date)] = json.loads(res)
        date += dt.timedelta(days=1)

    dir = f'./logs/{folder}'
    Path(dir).mkdir(parents=True, exist_ok=True)

    with open(f'{dir}/{today.strftime("%Y-%m-%d--%H-%M-%S.json")}', 'w') as outfile:
        json.dump(res_obj, outfile)



while True:
    print('\n ------- INITIALIZING -------')
    print('cph-hel init')
    create_logs('CPH-HEL', 'CPH-sky', 'HEL-sky')
    print('cph-hel is done')
    time.sleep(60)
    print('hel-cph init')
    create_logs('HEL-CPH', 'HEL-sky', 'CPH-sky')
    print('hel-cph is done')
    time.sleep(60)
    print('lond-usa init')
    create_logs('LOND-USA', 'LOND-sky', 'US-sky')
    print('lond-usa is done')
    print('\n ----------- DONE -----------')
    time.sleep(21600)
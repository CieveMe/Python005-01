import json
import sys

import requests


def get_url_name(url):
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 ' \
         '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'

    header = {'user-agent': ua}
    try:
        response = requests.get(url, headers=header)
    except requests.exceptions.ConnectTimeout as e:
        print(f'请求超时')
        sys.exit(1)

    data = response.json()['data']

    for i in data:
        for key, value in i.items():
            if key == 'target':
                print(value)


if __name__ == '__main__':
    myurl = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/film?limit=50&desktop=true'
    get_url_name(myurl)


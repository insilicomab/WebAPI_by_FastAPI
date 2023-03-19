import json

import requests


def main() -> None:
    url = 'http://127.0.0.1:8000/items/'
    body = {
        "name": "string",
        "description": "string",
        "price": 5980,
        "tax": 1.1,
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())


if __name__ == '__main__':
    main()
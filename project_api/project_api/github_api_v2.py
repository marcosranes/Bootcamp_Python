import requests


def avatar_github(username: str) -> dict:
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    dct = avatar_github('gvanrossum')
    for k, v in dct.items():
        print(f'{k}: {v}')

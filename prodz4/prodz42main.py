import requests

def init_ya_disk():
    with open('../secdata.txt') as f:
        token_ya = str(f.readline()).strip()
        print(f'Yandex API Token - {token_ya}')
        return token_ya

def create_folder(ya_token, folder_name):
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params={
                                    'path': folder_name,
                                },
                                headers={
                                    'Authorization': f"OAuth {ya_token}"
                                })

    print(response.status_code)
    return response.status_code

def delete_folder(ya_token, folder_name):
    response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                params={
                                    'path': folder_name,
                                },
                                headers={
                                    'Authorization': f"OAuth {ya_token}"
                                })

    print(response.status_code)
    return response.status_code

def get_folder(ya_token, folder_name):
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                params={
                                    'path': folder_name,
                                },
                                headers={
                                    'Authorization': f"OAuth {ya_token}"
                                })

    print(response.status_code)
    return response.status_code

if __name__ == "__main__":
    get_folder(init_ya_disk(), '1234')
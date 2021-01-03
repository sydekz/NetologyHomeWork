import requests
TOKEN = 'AgAEA7qh1JnTAADLW-89hKrUkUdpuwmqvCO8veY'
class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        """Метод загруджает файл file_path на яндекс диск"""
        filename = file_path.split('\\')[-1]
        print(filename)
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={
                                    'path': filename,
                                    'overwrite': 'true'
                                },
                                headers={
                                    'Authorization': f"OAuth {self.token}"
                                })
        # Тут ваша логика
        response.raise_for_status()
        href = response.json()['href']

        with open(filename, "rb") as f:
            put_response = requests.put(href, f)
        return put_response


if __name__ == '__main__':
    uploader = YaUploader(TOKEN)
    result = uploader.upload("test1.py")
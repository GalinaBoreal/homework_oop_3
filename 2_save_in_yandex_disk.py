import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        """Метод запрашивает URL для загрузки"""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        """Метод загружает файл на яндекс диск"""

        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk('test.txt', 'test.txt')

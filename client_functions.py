def upload_file(file_name):
    import requests
    x = requests.post(url="http://127.0.0.1:8000/uploadFile", files={"file_data": open(file_name, 'rb')}, headers={"fileName": file_name})
    return x.text

def download_file(file_id):
    import requests
    file_name = requests.get(url="http://127.0.0.1:8000/getFileName", params={"fileId": file_id})
    file = requests.get(url="http://127.0.0.1:8000/downloadFile", params={"fileId": file_id})
    print(file.content)
    open(file_name.json(), 'wb').write(file.content)
    return file_name.text


def list_all_files():
    import requests
    x = requests.get(url="http://127.0.0.1:8000/listAllFiles")
    return x.json()


def search_file(file_name):
    import requests
    results = requests.get(url="http://127.0.0.1:8000/searchFile", params={"fileName": file_name})
    return results.json()



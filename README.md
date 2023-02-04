# FileCloudAPI
My file cloud API is a set of programming instructions that allow software to interact with my file cloud services. This includes retrieving files from my file cloud, uploading files to my file cloud, and managing files in my file cloud. My file cloud API is designed to work with a variety of programming languages, including Java, Python, and PHP.

## Features

- List all files
- Download file
- Upload file
- Search file
- Delete file


## Installation

Cloning the repo.
```bash
git clone https://github.com/horapusa-lk/FileCloudAPI
cd FileCloudAPI
```

Creating virtual environment

```bash
py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env

```
    
Activating virtual environment

```bash
.\env\Scripts\activate
```

install requirements
```bash
pip3 install -r requirements.txt
```


## Run API

Run main.py

```bash
  python main.py
```



## API Reference

#### List all files

```http
  GET /listAllFiles
```

#### Upload a file

```http
  POST /uploadFile
```

| Header | File | Type     | Description                       |
| :-------- | :------- | :------- | :-------------------------------- |
| `fileName`     | - | `string` | **Required**. Name of the file |
| -     | `fileData`| `bytes` | **Required**. File data |

#### Delete a file

```http
  DELETE /deleteFile
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileId`      | `int` | **Required**. Id of the file |

#### Download a file

```http
  GET /downloadFile
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. Name of the file |

#### Get file name

```http
  GET /getFileName
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileId`      | `string` | **Required**. Name of the file |

#### Search file

```http
  GET /searchFile
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. Name of the file |

## Usage/Examples

#### Upload file

```python
def upload_file(file_name):
    import requests
    if "/" in file_name:
        file_n = file_name.split("/")[-1]
    if "//" in file_name:
        file_n = file_name.split("//")[-1]
    if "\\" in file_name:
        file_n = file_name.split("\\")[-1]
    else:
        file_n = file_name
    x = requests.post(url="http://127.0.0.1:8000/uploadFile", files={"fileFata": open(file_name, 'rb')}, headers={"fileName": file_n})
    return x.text
```

#### Download file

```python
def download_file(file_id):
    import requests
    file_name = requests.get(url="http://127.0.0.1:8000/getFileName", params={"fileId": file_id})
    file = requests.get(url="http://127.0.0.1:8000/downloadFile", params={"fileId": file_id})
    print(file.content)
    open(file_name.json(), 'wb').write(file.content)
    return file_name.text
```

#### List all files

```python
def list_all_files():
    import requests
    x = requests.get(url="http://127.0.0.1:8000/listAllFiles")
    return x.json()
```

#### Search file

```python
def search_file(file_name):
    import requests
    results = requests.get(url="http://127.0.0.1:8000/searchFile", params={"fileName": file_name})
    return results.json()
```



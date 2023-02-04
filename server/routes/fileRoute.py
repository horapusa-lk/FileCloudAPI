from fastapi import APIRouter, File, Header
from fastapi.responses import FileResponse

from typing import Union
from server.controllers.fileController import FileController
router = APIRouter()
fc = FileController()


def returnError(error_code, error_message):
    return {
        "error": {
            "code": error_code,
            "message": error_message
        }

    }


@router.post("/uploadFile")
def create_file(fileName: Union[str, None] = Header(default=None), file_data: bytes = File()):
    print(fileName)
    return fc.create_file(file_name=fileName, file_data=file_data)


@router.get("/listAllFiles")
def list_all_file():
    return fc.list_files()


@router.delete("/deleteFile")
def list_all_file(fileId: int):
    return fc.delete_file(file_id=fileId)


@router.get("/searchFile")
def list_all_file(fileName):
    return fc.search_file(file_name=fileName)


@router.get("/downloadFile", response_class=FileResponse)
def download_file(fileId: int):
    return fc.recive_file(file_id=fileId)


@router.get("/getFileName")
def get_file_name(fileId: int):
    return fc.get_file_name(file_id=fileId)



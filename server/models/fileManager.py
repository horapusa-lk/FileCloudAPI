import json


class FileManager:

    def db_add(self, file_name, file_id):
        import os
        from datetime import datetime
        file_size = os.stat(f"server/storage/{file_id}").st_size
        if file_size > 1073741823:
            file_size = file_size / 1024 / 1024 / 1024
            file_size = f"{file_size} GB"
        elif file_size > 1048575:
            file_size = file_size / 1024 / 1024
            file_size = f"{file_size} MB"
        elif file_size > 1024:
            file_size = file_size / 1024
            file_size = f"{file_size} KB"
        else:
            file_size = f"{file_size} Bytes"
        created_date = str(datetime.now())
        with open("server/config/data.json") as json_file:
            json_object = json.load(json_file)
        file_info = {
            "fileId": file_id,
            "fileName": file_name,
            "fileSize": file_size,
            "createdDate": created_date,
            "deleted": False
        }
        json_object.append(file_info)
        json_object = json.dumps(json_object, indent=4)
        with open("server/config/data.json", "w") as outfile:
            outfile.write(json_object)

    def create_file(self, file_name: str, file_data: bytes):
        with open("server/config/data.json") as json_file:
            json_object = json.load(json_file)
            file_id = len(json_object)
        with open(f"server/storage/{file_id}", "wb") as file:
            file.write(file_data)
        self.db_add(file_name=file_name, file_id=file_id)

    def list_files(self):
        with open("server/config/data.json") as json_file:
            json_object = json.load(json_file)
        file_list = []
        for file in json_object:
            if not file["deleted"]:
                file_list.append({
                    "fileId": file["fileId"],
                    "fileName": file["fileName"],
                    "createdDate": file["createdDate"]
                })
        return file_list

    def delete_file(self, file_id):
        with open("server/config/data.json") as json_file:
            json_object = json.load(json_file)
        count = 0
        for file in json_object:
            if file_id == file["fileId"]:
                json_object[count]["deleted"] = True
            count += 1
        json_object = json.dumps(json_object, indent=4)
        with open("server/config/data.json", "w") as outfile:
            outfile.write(json_object)

    def recive_file(self, file_id):
        file = f"server/storage/{file_id}"
        return file


def success_response(message):
    return {
        "success": True,
        "message": message
    }


def error_response(code, message):
    return {
        "error": code,
        "message": message
    }

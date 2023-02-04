from server.models.fileManager import FileManager, success_response, error_response

fm = FileManager()


class FileController:
    def create_file(self, file_name: str, file_data: bytes):
        try:
            fm.create_file(file_name=file_name, file_data=file_data)
            return success_response("File created successfully.")
        except:
            return error_response(500, "Server Error")

    def list_files(self):
        try:
            return fm.list_files()
        except:
            return error_response(500, "Server Error")

    def delete_file(self, file_id):
        try:
            fm.delete_file(file_id)
            return success_response("File deleted successfully.")
        except:
            return error_response(500, "Server Error")

    def recive_file(self, file_id):
        try:
            return fm.recive_file(file_id)
        except:
            return error_response(404, "File not found")

    def search_file(self, file_name):
        match_list = []
        for file in self.list_files():
            if file_name in file["fileName"]:
                match_list.append(file)
        if not match_list == []:
            return match_list
        else:
            return error_response(404, "File not found")

    def get_file_name(self, file_id):
        for file in self.list_files():
            if file["fileId"] == file_id:
                return file["fileName"]
        return error_response(404, "File not found")


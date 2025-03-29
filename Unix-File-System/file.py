from datetime import datetime 
from file_type import FileType

class File:
    def __init__(self, name: str, file_type: FileType, size: int, 
                 created_at: datetime, modified_at: datetime, content: str = None):
        self.name = name
        self.file_type = file_type
        self.size = size
        self.content = content
        self.created_at = created_at
        self.modified_at = modified_at
        self.permissions = {
            'read': True,
            'write': False,
            'execute': False
        }
        self.is_directory = (file_type == FileType.DIRECTORY)
        self.children = [] if self.is_directory else None
        self.parent = None
    
    def add_file(self, file):
        if self.is_directory:
            file.parent = self
            self.children.append(file)
        else:
            raise Exception("Cannot add file to a non-directory")
    
    def remove_file(self, file):
        if self.is_directory:
            self.children.remove(file)
        else:
            raise Exception("Cannot remove file from a non-directory")
    
    def get_file_name(self):
        return self.name

    def get_file_type(self):
        return self.file_type
    
    def get_file_size(self):
        return self.size
    
    def get_file_content(self):
        return self.content
    
    def get_created_at(self):
        return self.created_at
    
    def get_modified_at(self):
        return self.modified_at
    
    def get_full_path(self):
        if self.parent:
            return f"{self.parent.get_full_path()}/{self.name}"
        return self.name
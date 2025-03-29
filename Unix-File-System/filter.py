from abc import ABC, abstractmethod
from file import File
from file_type import FileType
from datetime import datetime
from typing import List, Optional
class Filter(ABC):
    """
    Abstract base class for filters.
    """
    def apply(self, root: File) -> File:
        """
        Apply the filter to the given data.
        """
        pass

class FileTypeFilter(Filter):
    """
    Filter for file types.
    """
    def __init__(self, file_type: FileType):
        self.file_type = file_type
    
    def apply(self, file: File):
        """
        Apply the file type filter to the given data.
        """
        if file.get_file_type() == self.file_type:
            return file
        return None

class FileSizeFilter(Filter):
    """
    Filter for file sizes.
    """
    def __init__(self, size: int):
        self.size = size
    
    def apply(self, file: File):
        """
        Apply the file size filter to the given data.
        """
        if file.get_file_size() == self.size:
            return file
        return None

class FileNameFilter(Filter):
    """
    Filter for file names.
    """
    def __init__(self, name: str):
        self.name = name
    
    def apply(self, file: File):
        """
        Apply the file name filter to the given data.
        """
        if self.name in file.get_file_name():
            return file
        return None
    
class DateFilter(Filter):
    """
    Filter for file dates.
    """
    def __init__(self, date: datetime, field: str = "modified", operator: str = "="):
        """
        Initialize with date, field (modified or created), and operator.
        """
        self.date = date
        self.field = field
        self.operator = operator
    
    def matches(self, file: File) -> bool:
        if self.field == "modified":
            file_date = file.get_modified_at()
        else:  # created
            file_date = file.get_created_at()
            
        if self.operator == "=":
            return file_date.date() == self.date.date()
        elif self.operator == ">":
            return file_date > self.date
        elif self.operator == "<":
            return file_date < self.date
        elif self.operator == ">=":
            return file_date >= self.date
        elif self.operator == "<=":
            return file_date <= self.date
        return False
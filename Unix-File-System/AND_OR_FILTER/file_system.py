from file import File
from filter import Filter
from typing import List, Literal
from datetime import datetime

class FileSystem:
    def __init__(self):
        self.filters = []
        
    def add_filter(self, filter: Filter):
        """
        Add a filter to the file system.
        """
        self.filters.append(filter)
        
    def search(self, root: File, logic: str) -> List[File]:
        """
        Search for files in the file system that match the filters using AND/OR logic.
        """
        results = []
        self._search_recursive(root, results, logic)
        return results
    
    def _search_recursive(self, file: File, results: List[File], logic: str):
        """
        Search for files in File System recursively across all files and folders in the file system 
        Logic represents the use of either AND/OR Logic 
        """
        if self.filters:
            match = self._apply_filter(file, logic)
            if match:
                results.append(file)
        
        # If File is a directory 
        if file.is_directory:
            for child in file.children:
                self._search_recursive(child, results, logic)
    
    def _apply_filter(self, file: File, logic: str):
        """
        Function to apply file system filters based on the logic provided
        """
        if logic == 'OR':
            for filter in self.filters:
                if filter.apply(file):
                    return True
            return False
        else:
            for filter in self.filters:
                if not filter.apply(file):
                    return False
            return True
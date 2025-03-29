from file import File
from filter import Filter
from typing import List
from datetime import datetime

class FileSystem:
    def __init__(self):
        self.filters = []
        
    def add_filter(self, filter: Filter):
        """
        Add a filter to the file system.
        """
        self.filters.append(filter)
        
    
    def search(self, root: File) -> List[File]:
        """
        Search for files in the file system that match the filters.
        """
        results = []
        self._search_recursive(root, results)
        return results
    
    def _search_recursive(self, file: File, results: List[File]):
        """
        Recursively search for files in the file system that match the filter
        """
        for filter in self.filters:
            result = filter.apply(file)
            if result:
                results.append(result)
        
        if file.is_directory:
            for child in file.children:
                self._search_recursive(child, results)
        return results 
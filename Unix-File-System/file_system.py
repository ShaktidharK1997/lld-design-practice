from file import File
from filter import Filter
from typing import List
from datetime import datetime
class FileSystem:
    def __init__(self, root: File):
        self.root = root
        self.filters = []
        
    def add_filter(self, filter: Filter):
        """
        Add a filter to the file system.
        """
        self.filters.append(filter)
        
    
    def search(self, filters: List[Filter] = None) -> List[File]:
        """
        Search for files that match all the given filters.
        """
        if filters is None:
            filters = []
        
        results = []
        self._search_recursive(self.root, filters, results)
        return results
    
    def _search_recursive(self, current: File, filters: List[Filter], results: List[File]):
        """
        Recursively search for files that match all filters.
        """
        # Check if current file matches all filters
        if all(f.matches(current) for f in filters):
            results.append(current)
        
        # If directory, search children
        if current.is_directory and current.children:
            for child in current.children:
                self._search_recursive(child, filters, results)
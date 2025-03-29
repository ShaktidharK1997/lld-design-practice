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
        
    def clear_filters(self):
        """
        Clear all filters from the file system.
        """
        self.filters = []
    
    def search(self, root: File, logic: Literal["AND", "OR"] = "OR") -> List[File]:
        """
        Search for files in the file system that match the filters.
        
        Parameters:
            root: The root file or directory to start searching from
            logic: The logic to apply when combining filters, either "AND" or "OR"
            
        Returns:
            A list of files that match the filter criteria
        """
        results = []
        self._search_recursive(root, results, logic)
        return results
    
    def _search_recursive(self, file: File, results: List[File], logic: str):
        """
        Recursively search for files in the file system that match the filters.
        
        Parameters:
            file: The current file or directory being processed
            results: The list to store matching files
            logic: The logic to apply when combining filters ("AND" or "OR")
        """
        # Skip filtering if we have no filters
        if self.filters:
            matches = self._apply_filters(file, logic)
            if matches:
                results.append(file)
        
        # Recursively process children if this is a directory
        if file.is_directory:
            for child in file.children:
                self._search_recursive(child, results, logic)
    
    def _apply_filters(self, file: File, logic: str) -> bool:
        """
        Apply filters to a file using the specified logic.
        
        Parameters:
            file: The file to apply filters to
            logic: The logic to use when combining filters ("AND" or "OR")
            
        Returns:
            True if the file matches the filter criteria, False otherwise
        """
        if not self.filters:
            return True
            
        if logic == "AND":
            # File must match ALL filters
            for filter in self.filters:
                if not filter.apply(file):
                    return False
            return True
        else:  # "OR" logic
            # File must match ANY filter
            for filter in self.filters:
                if filter.apply(file):
                    return True
            return False
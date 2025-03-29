You need to design a system that can search for files in a Unix-like directory structure based on various criteria such as:

File name (with support for wildcards)
File size (greater than, less than, exact)
File modification date
File type (regular file, directory, symbolic link, etc.)
File content (text search)

Your solution should be extensible so that new search criteria can be added easily. The system should be efficient and maintainable.

Clarify requirements 

I'd like to use Python. Before I get started, I would like to clarify certain things 

1. So it is a unix file system where it is a heirarchial folder structure with files and folders in it? 
2. What other file attributes do i need to track? I can think of file name, file type, file size, date created, date modified, file content 
3. Since we are going to search file content, I assume I will need to implement file handling for my file system? 


Yes, we're working with a Unix-like hierarchical file system with folders (directories) and files.
The file attributes you've identified are spot on. We'll need to track:

File name
File type (regular file, directory, symbolic link)
File size (in bytes)
Date created
Date modified
File permissions
File content (for text files)

Yes, you'll need to implement file handling to search within file contents. This would involve opening and reading files to perform text searches.


High level Design (Classes, Interfaces and Enumerations)
1. File Class 
- File attributes (name, type, size, date_created, date_modified, permissions, is_directory, children)
- - is_directory flag to check if it's a directory
- - children : to store file objects if it is a directory 
- methods 
- - get_name : return name of file 
- - get_type : return type of file 
- - get_size : return size of file 
- - date_created : return creation date 
- - date_modified : return modified date 
- - permissions : return permissions of file 

2. Filter class : Abstract class 

3. Each specific filter will be a inherited class of Filter Class with the specific filter condition 

4. File System Class 
- attributes : filters list (list of created filter objects)
- methods 
- - add_filter(filter)
- - apply_filter(filter_name, root_file) : applies filter to root obbject

5. We can also have an enum of the file types to be supported by our file system
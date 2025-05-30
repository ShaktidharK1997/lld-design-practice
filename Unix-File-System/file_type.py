from enum import Enum
class FileType(Enum):
    """Enum for file types."""
    TEXT = ".txt"  
    IMAGE = '.jpg'
    DIRECTORY = '.dir'
    PDF = '.pdf'
    AUDIO = '.mp3'
    VIDEO = '.mp4'
    ARCHIVE = '.zip'


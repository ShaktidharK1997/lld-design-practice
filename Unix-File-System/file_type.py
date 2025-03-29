class FileType(Enum):
    """Enum for file types."""
    TEXT = ".txt"  
    IMAGE = '.jpg'
    DIRECTORY = '.dir'
    PDF = '.pdf'
    AUDIO = '.mp3'
    VIDEO = '.mp4'
    ARCHIVE = '.zip'

    def __str__(self):
        return self.name.lower()
class ProjectFile:
    def __init__(self, file_path: str):
        self._file_path: str = file_path

    @property
    def file_path(self):
        return self._file_path

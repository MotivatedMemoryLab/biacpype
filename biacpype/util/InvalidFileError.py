class InvalidFileError(Exception):
    """InvalidFileError used for validation purpose
    """
    def __init__(self, msg, filename):
        self.msg = msg
        self.filename = filename

    def __str__(self):
        return (repr(self.msg))

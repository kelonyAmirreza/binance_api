class Error(Exception):
    pass


class ParamNotSupportedError(Error):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f'{self.param} is provided, but is not supported.'

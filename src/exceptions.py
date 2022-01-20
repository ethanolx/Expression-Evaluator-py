class InvalidOptionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InputError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

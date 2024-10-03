class CharCodeNotFoundError(Exception):
    def __init__(self, char_code: str):
        self.char_code = char_code

    def __str__(self) -> str:
        return f"Char code not found: {self.char_code}"

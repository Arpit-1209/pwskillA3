class CustomError(Exception):
    def __init__(self, message):
        self.message = message

raise CustomError("This is a custom error message.")

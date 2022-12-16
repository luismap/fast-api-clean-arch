


class CreatePostError(Exception):
    """Error creating Post"""

class IdNotFound(Exception):
    def __init__(self, id: int, message="id not not found"):
        """
        General exception when id is not found.

        Args:
            id (int): input id 
            message (str, optional): input message. Defaults to "id not not found".
        """
        self.id = id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.id} -> {self.message}'
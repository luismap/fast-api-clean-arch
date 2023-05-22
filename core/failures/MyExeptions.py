


class CreatePostError(Exception):
    """Error creating Post"""

class UpdatePostException(Exception):
    def __init__(self, id: int, message="cannot update other post"):
        """
        Cannot update other Posts Exception.

        Args:
            id (int): post id to delete
            message (str, optional): input message. Defaults to "cannot update others post".
        """
        self.id = id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.id} -> {self.message}'

class DeletePostException(Exception):
    def __init__(self, id: int, message="cannot delete other post"):
        """
        Cannot delete other Posts Exception.

        Args:
            id (int): post id to delete
            message (str, optional): input message. Defaults to "cannot delete others post".
        """
        self.id = id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.id} -> {self.message}'


class IdNotFound(Exception):
    def __init__(self, id: int, message="id not found"):
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
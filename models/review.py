#!usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

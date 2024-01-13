#!usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    loaded_objects = json.load(file)
                    for key, value in loaded_objects.items():
                        class_name, instance_id = key.split('.')
                        class_obj = globals()[class_name]
                        instance = class_obj(**value)
                        FileStorage.__objects[key] = instance
                except json.JSONDecodeError:
                    pass

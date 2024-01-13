"""Module for HBNBCommand class."""
import cmd
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB project."""
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl-D)"""
        print()
        return True

    def do_help(self, arg):
        """To get help on a command, type help <topic>."""
        return super().do_help(arg)

    def handle_empty_line(self, line):
        """Eliminates empty lines"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it,
        and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval("{}()".format(arg))
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in FileStorage._FileStorage__objects:
                print(FileStorage._FileStorage__objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in FileStorage._FileStorage__objects:
                del FileStorage._FileStorage__objects[key]
                FileStorage().save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        objects = FileStorage._FileStorage__objects
        result = [str(obj) for obj in objects.values()
                  if type(obj).__name__ == args[0]]
        print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0],
                            args[1]) not in FileStorage._FileStorage__objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = FileStorage._FileStorage__objects[key]
            setattr(obj, args[2], eval(args[3]))
            FileStorage().save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

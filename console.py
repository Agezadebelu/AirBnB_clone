#!/usr/bin/env python3
"""Module for HBNBCommand class."""
import cmd
import re
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB project."""
    
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl-D)"""
        print()  # Print a newline before exiting
        return True

    def do_help(self, arg):
        """To get help on a command, type help <topic>."""
        return super().do_help(arg)
    
    def handle_empty_line(self, arg):
        """Eliminates empty lines"""
        return False
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
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
            if key in storage.all():
                print(storage.all()[key])
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
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        result = [str(obj) for obj in objects.values() if type(obj).__name__ == args[0]]
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
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[key]
            setattr(obj, args[2], eval(args[3]))
            storage.save()

    def default(self, arg):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", arg)
        self._precmd(arg)

    def _precmd(self, arg):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", arg)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def do_count(self, arg):
        """Counts the instances of a class.
        """
        words = arg.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in self.valid_classes:
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()


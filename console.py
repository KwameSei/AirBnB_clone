#!/usr/bin/env python3
"""A console module"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """class definition for the console commands"""

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_EOF(self, line):
        """"Command to exit from the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Parses the previous command entered"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        cls = self.parseline(line)[0]
        if cls is None:
            print("** class name missing **")
        elif cls not in self.classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(cls)()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id"""
        cls = self.parseline(line)[0]
        cls_id = self.parseline(line)[1]
        if cls is None:
            print("** class name missing **")
        elif cls not in self.classes:
            print(" ** class doesn't exist **")
        elif cls_id == "":
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if cls_id == value.id:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
        cls = self.parseline(line)[0]
        cls_id = self.parseline(line)[1]
        if cls is None:
            print("** class name missing **")
        elif cls not in self.classes:
            print(" ** class doesn't exist **")
        elif cls_id == "":
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if cls_id == value.id:
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        cls = self.parseline(line)[0]
        if line != "" and cls not in self.classes:
            print("** class doesn't exist **")
        else:
            new_list = []
            for obj in storage.all().values():
                if cls in self.classes or line == "":
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, line):
        """Update an instance based on class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        terms = shlex.split(line, posix=False)
        if terms[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(terms) < 2:
            print("** instances id missing **")
            return
        key = "{}.{}".format(terms[0], terms[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(terms) < 3:
            print("** attribute name missing **")
            return
        elif len(terms) < 4:
            print("** value missing **")
            return
        terms[3] = terms[3].strip("\"")
        storage.all()[key].__dict__[terms[2]] = terms[3]
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

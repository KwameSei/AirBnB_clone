#!/usr/bin/env python3
"""A console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class definition for the console commands"""

    prompt = "(hbnb) "
    classes = ['BaseModel']

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
        if line is not "" and cls not in self.classes:
            print("** class doesn't exist **")
        else:
            new_list = []
            for obj in storage.all().values():
                if cls in self.classes or line == "":
                    new_list.append(obj.__str__())
            print(new_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

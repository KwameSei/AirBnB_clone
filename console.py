#!/usr/bin/env python3
'''A console module'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''class definition for the console commands'''

    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''quits the program'''
        return True

    def do_quit(self, line):
        '''quits the program'''
        return True

    def help_quit(self):
        '''Gives description of the commands users search help on'''
        print("Quit command to exit the program")

    def help_EOF(self):
        '''Gives description of the commands users search help on'''
        print("EOF command to exit the program")

    def emptyline(self):
        '''Parses the previous command entered'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

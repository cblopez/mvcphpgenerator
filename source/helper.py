import os
from sys import exit
from constants import *

def process_directory(directory):
    '''
    Ensures the directory does not end with a back-slash
    @Param directory: directory to process
    @return: Directory on desired format
    '''
    if directory.endswith("/") or directory.endswith("\\"):
        return directory[:-1]
    else:
        return directory

def test_directory(directory):
    '''
    Checks if there is an existing directory with that path.
    If there is not a directory, it asks the user if he wants to create it.
    If the user doesn't create it, then the app shuts down and asks for a valid directory.
    @Param directory: Directory to validate
    '''
    directory = process_directory(directory)
    if(os.path.isdir(directory)):
        print("[+] Valid directory: %s" % directory)
    else:
        answer = ""
        while answer not in ['y', 'n', 'Y', 'N']:
            answer = raw_input("[?] The existing directory does not exist, would you like to create one? [y/n]: ")

        if answer in ['y','Y']:
            print("[+] Trying directory creation on: %s" % directory)
            try:
                os.makedirs(directory)
            except OSError as e:
                if(e.errno != e.errno.EEXIST):
                    raise
            print("[+] Directory created successfully.")
        else:
            print("[!] Could not use given directory. Exiting...")
            exit()

def test_file(file):
    '''
    Checks if a given files exists on the system
    @Param file: File path to check
    '''
    try:
        input_file = open(file, 'r')
    except FileNotFoundError as e:
        print("[!] The given file does not exist, please select a valid one. Exiting...")
    input_file.close()

def process_input_file(input_file):
    '''
    Wraps the content of the given file into entities, attributes and actions.
    @Param input_file: File to process
    @return: Structured dictionary containing all the information from the file-
    '''
    structured_file = open(input_file, 'r')
    entities_dict = {}
    file_lines = [x.strip() for x in structured_file.readlines()]
    currentEntity = ""
    currentLine = 1
    for line in file_lines:
        if line.startswith("-"):
            currentEntity = line[1:]
            entities_dict[currentEntity] = {}
            entities_dict[currentEntity]['attributes'] = []
            entities_dict[currentEntity]['actions'] = []
            print("[+] Found entity: %s" % currentEntity)
        elif line.startswith("+"):
            currentAttribute = line[1:]
            entities_dict[currentEntity]['attributes'].append(currentAttribute)
            print("\t[+]Found attribute: %s" % currentAttribute)
        elif line.startswith("*"):
            currentAction = line[1:]
            entities_dict[currentEntity]['actions'].append(currentAction)
            print("\t[+]Found action: %s" %currentAction)
        else:
            print("[!] Syntax error on line: %d. Check if there is a syntax error. Exiting..." % currentLine)
            exit()
        currentLine+=1

    return entities_dict

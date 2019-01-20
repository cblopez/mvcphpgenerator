import os
import argparse

from sys import argv, exit
from controller import generateController
from model import generateModel
from index import createIndex
from gatherData import *
from helper import *
from database import *
from constants import *


def main():

    reader = argparse.ArgumentParser(description="mvcPHPGenerator. PHP file generator.")

    reader.add_argument("-i",               dest="input_file", required=True, default=None, help="Select entities, attributes and actions from a structured file. Visit http://www.github.com/cblopez/mvcPHPGenerator for more details.")
    reader.add_argument("-o",               dest="output_directory", required=False, default=None, help="Select the output directory of the resulting folder. Default: \'.\'")
    reader.add_argument("--name",           dest="output_name", required=False, default=None, help="Select the name of the output directory you want to create. Default: \'MVCPHPGenerator\'")
    reader.add_argument("--create-index",   dest="index", action="store_true", required=False, help="Enable de index.php creation.")

    arguments = reader.parse_args()

    if arguments.output_directory is not None:
        output_directory = arguments.output_directory
        output_directory = process_directory(output_directory)
        test_directory(output_directory)
    else:
        # Script execution path
        output_directory = os.path.dirname(os.path.abspath(__file__))

    if arguments.output_name is not None:
        output_name = arguments.output_name
    else:
        output_name = "MVCPHPGenerator"

    absolute_output_path = output_directory + '/' + output_name

    print("")
    print("*_*_*_*_*_*_*_*_*_*")
    print("MVC PHP Generator")
    print("by Christian Barral")
    print("*_*_*_*_*_*_*_*_*_*")
    print("")

    print("[+] Starting MVC PHP Generator")
    print("[+] Checking input file")
    test_file(arguments.input_file)
    entities_dict = process_input_file(arguments.input_file)

    print("[+] Creating directory structure")

    # Use try-except to catch any error dispite dir existance, due to a race condition when checking the directory.
    try:
        os.mkdir(absolute_output_path)
    except OSError, e:
        if e.errno != os.errno.EEXIST:
            raise

    print("[+] Created " + output_name + " folder on " + output_directory)
    try:
        os.mkdir(absolute_output_path + '/Controllers')
    except OSError, e:
        if e.errno != os.errno.EEXIST:
            raise

    print("[+] Created Controllers folder")
    try:
        os.mkdir(absolute_output_path + '/Functions')
    except OSError, e:
        if e.errno != os.errno.EEXIST:
            raise

    print("[+] Created Functions folder")
    try:
        os.mkdir(absolute_output_path + '/Models')
    except OSError, e:
        if e.errno != os.errno.EEXIST:
            raise

    print("[+] Created Models folder")
    try:
        os.mkdir(absolute_output_path + '/Views')
    except OSError, e:
        if e.errno != os.errno.EEXIST:
            raise

    print("[+] Created config folder")
    try:
        os.mkdir(absolute_output_path + '/config')
    except OSError, e:
        if e.errno != os.errno.EEXIST:
            raise

    print("[+] Created Views folder")


    print("[+] Creating gatherData.php")
    createGatherData(absolute_output_path, [key for key in entities_dict])

    print("[+] Creating Database.php class")
    createDatabase(absolute_output_path)

    for key in entities_dict:
        entityName = key
        attributesList = []
        actionList = []
        for attribute in entities_dict[key]['attributes']:
            attributesList.append(attribute)
        for action in entities_dict[key]['actions']:
            actionList.append(action)
        print("[+] Creating Controller for %s" % entityName)
        generateController(entityName, actionList, absolute_output_path)
        print("[+] Creating Model for %s" % entityName)
        generateModel(entityName, attributesList, absolute_output_path)
        print("[+] Appending to gatherData.php for %s" % entityName)
        appendToGatherData(entityName, attributesList, absolute_output_path)

    closeGatherData(absolute_output_path)
    print("[+] Creating index.php")
    if arguments.index:
        createIndex(absolute_output_path)
    print("[+] Finished successfully.")
    print("IMPORTANT: Go to the Functions folder and fill the models includes from gatherData.php manually. ")


if __name__ == '__main__':
    main()

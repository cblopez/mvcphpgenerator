import os

def generateController(entityName,actionList):
    '''
    Controller Generator
    '''
    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "_")

    controller = open('./MVCPHPGenerator/Controllers/' + entityName + "_Controller.php", 'w')

    controller.write('<?php\r\n')
    controller.write('\r\n')
    controller.write('include __DIR__.\'../Functions/gatherData.php\';\r\n')
    controller.write('\r\n')
    controller.write('\r\n')
    controller.write('if(!$_GET){\r\n')
    controller.write('\t//Fill\r\n')
    controller.write('}\r\n')
    controller.write('\r\n')
    controller.write('else{\r\n')
    controller.write('\r\n')
    controller.write('\tswitch($_GET[\'action\']){\r\n')
    controller.write('\r\n')
    for action in actionList:
        controller.write('\t\tcase \'' + action + '\':\r\n')
        controller.write('\t\tif(!$_POST){\r\n')
        controller.write('\t\t\t//Fill\r\n')
        controller.write('\t\t} else {\r\n')
        controller.write('\t\t\t//Fill\r\n')
        controller.write('\t\t}\r\n')
        controller.write('\t\tbreak;\r\n')
        controller.write('\r\n')
    controller.write('\t}\r\n')
    controller.write('}\r\n')
    controller.write('\r\n')
    controller.write('?>\r\n')

    controller.close()

def generateModel(entityName, attributesList):
    '''
    Model Generator
    '''
    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "_")

    model = open('./MVCPHPGenerator/Models/' + entityName + "_Model.php", 'w')

    model.write('<?php\r\n')
    model.write('\r\n')
    model.write('class ' + entityName + '_Model{\r\n')
    model.write('\r\n')
    for attribute in attributesList:
        model.write('\tvar $' + attribute +';\r\n')
    model.write('\tvar $db;\r\n')
    model.write('\r\n')
    model.write('\tfunction __construct(')
    for i in range(0,len(attributesList)):
        model.write('$' + attributesList[i])
        if i != (len(attributesList) - 1):
            model.write(',')
    model.write('){\r\n')
    for attribute in attributesList:
        model.write('\t\t$this->' + attribute + ' = $' + attribute + ';\r\n')
    model.write('\t\tinclude_once __DIR__.\'/../Functions/FillWithDBConnectioin.php\';\r\n')
    model.write('\t\t$this->db = //Fill with connection method\r\n')
    model.write('\t}\r\n')
    model.write('\r\n')
    model.write('}\r\n')
    model.write('?>\r\n')

    model.close()

def createGatherData():
    '''
    Gather Data initial unfilled script
    '''

    gather = open('./MVCPHPGenerator/Functions/gatherData.php', 'w')

    gather.write('<?php\r\n')
    gather.write('\r\n')
    gather.write('//Fill with includes\r\n')
    gather.write('\r\n')

    gather.close()

def appendToGatherData(entityName, attributesList):
    '''
    Append to gatherData.php file
    '''
    originalName = entityName
    originalName = originalName.lower()
    originalName = originalName.title()
    originalName = originalName.replace(" ", "_")
    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "")

    gather = open('./MVCPHPGenerator/Functions/gatherData.php', 'a+')

    gather.write('function gatherData' + entityName + '(){\r\n')
    gather.write('\r\n')
    for attribute in attributesList:
        gather.write('\t$' + attribute + ' = \'\';\r\n')
    gather.write('\r\n')
    gather.write('\tif($_POST){\r\n')
    gather.write('\r\n')
    for attribute in attributesList:
        gather.write('\t\tif(isset($_POST[\'' + attribute + '\'])) $' + attribute + ' = $_POST[\'' + attribute + '\'];\r\n')
    gather.write('\r\n')

    gather.write('\t\treturn new ' + originalName + '_Model(')
    for i in range(0, len(attributesList)):
        gather.write('$' + attributesList[i])
        if i != (len(attributesList) - 1):
            gather.write(',')
    gather.write(');\r\n')
    gather.write('\r\n')
    gather.write('\t} else {\r\n')
    gather.write('\r\n')
    for attribute in attributesList:
        gather.write('\t\tif(isset($_GET[\'' + attribute + '\'])) $' + attribute + ' = $_GET[\'' + attribute + '\'];\r\n')
    gather.write('\r\n')
    gather.write('\t\treturn new ' + originalName + '_Model(')
    for i in range(0, len(attributesList)):
        gather.write('$' + attributesList[i])
        if i != (len(attributesList) - 1):
            gather.write(',')
    gather.write(');\r\n')
    gather.write('\r\n')
    gather.write('\t}\r\n')
    gather.write('\r\n')
    gather.write('}\r\n')
    gather.write('\r\n')

    gather.close()

def closeGatherData():
    '''
    Close PHP Tag on gatherData.php
    '''
    gather = open('./MVCPHPGenerator/Functions/gatherData.php', 'a+')

    gather.write('?>')

    gather.close()

def createIndex():
    '''
    Creates an index.php on the root directory of the output folder
    Note: the index.php will be used as a common entry point
    '''
    index = open('./MVCPHPGenerator/index.php', 'w')

    index.write('<?php\r\n')
    index.write('\r\n')
    index.write('define(\"DEFAULT_CONTROLLER\", \"Index\");\r\n')
    index.write('define(\"DEFAULT_ACTION\", \"index\");\r\n')
    index.write('\r\n')
    index.write('\r\n')
    index.write('function run(){\r\n')
    index.write('\ttry{\r\n')
    index.write('\t\tif(!isset($_GET[\"controller\"])){\r\n')
    index.write('\t\t\t$_GET[\"controller\"] = DEFAULT_CONTROLLER;\r\n')
    index.write('\t\t}\r\n')
    index.write('\t\tif(!isset($_GET[\"action\"])){\r\n')
    index.write('\t\t\t$_GET[\"action\"] = DEFAULT_ACTION;\r\n')
    index.write('\t\t}\r\n')
    index.write('\r\n')
    index.write('\t\t$controller = loadController($_GET[\"controller\"]);\r\n')
    index.write('\r\n')
    index.write('\t\tinclude (string)$controller;\r\n')
    index.write('\r\n')
    index.write('\t} catch(Exception $ex){\r\n')
    index.write('\t\tdie(\"An exception has occured: \" . $ex->getMessage());\r\n')
    index.write('\t}\r\n')
    index.write('}\r\n')
    index.write('\r\n')
    index.write('function loadController($controllerName){\r\n')
    index.write('\t$controllerClassName = __DIR__.\"/Controllers/\".$controllerName.\"_Controller.php\";\r\n')
    index.write('\treturn $controllerClassName;\r\n')
    index.write('}\r\n')
    index.write('\r\n')
    index.write('run();\r\n')
    index.write('?>\r\n');

    index.close();



def main():
    print("")
    print("*_*_*_*_*_*_*_*_*_*")
    print("MVC PHP Generator")
    print("by Christian Barral")
    print("*_*_*_*_*_*_*_*_*_*")
    print("")

    print("[+] Starting MVC PHP Generator")
    print("[+] Creating directory structure")
    os.mkdir('./MVCPHPGenerator')
    print("[+] Created MVCPHPGenerator folder")
    os.mkdir('./MVCPHPGenerator/Controllers')
    print("[+] Created Controllers folder")
    os.mkdir('./MVCPHPGenerator/Functions')
    print("[+] Created Functions folder")
    os.mkdir('./MVCPHPGenerator/Models')
    print("[+] Created Models folder")
    os.mkdir('./MVCPHPGenerator/Views')
    print("[+] Created Views folder")

    option = "yes"

    print("[+] Creating gatherData.php")
    createGatherData()

    while(option in ['y', 'Y', 'ye', 'Ye', 'yes', 'Yes']):
        entityName = raw_input("Entity name: ")
        attributesList = []
        attribute = ''
        while(attribute != 'exit'):
            attribute = raw_input('Insert attribute name (exit to stop): ')
            if(attribute != 'exit'):
                attributesList.append(attribute)
        actionList = []
        action = ''
        while(action != 'none'):
            action = raw_input('Insert action (none to stop): ')
            if(action != 'none'):
                actionList.append(action)

        print("[+] Creating Controller for %s" % entityName)
        generateController(entityName, actionList)
        print("[+] Creating Model for %s" % entityName)
        generateModel(entityName, attributesList)
        print("[+] Appending to gatherData.php for %s" % entityName)
        appendToGatherData(entityName, attributesList)

        option = raw_input("Would you like to add more entities? (yes/no): ")

    closeGatherData()
    print("[+] Creating index.php")
    createIndex()
    print("[+] Finished successfully.")
    print("IMPORTANT: Before using the project, please head to MVCPHPGenerator/Functions/gatherData.php and set the models includes" +
    " at the beginning of the script, where it says \'//Fill with includes\'")


main()

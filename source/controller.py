from constants import *

def generateController(entityName, actionList, absolute_output_path):
    '''
    Controller Generator given an entity name, an action list and the output path
    @Param entityName: Name of the controller
    @Param actionList: List of actions that the controller will support
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "_")

    controller = open(absolute_output_path + '/Controllers/' + entityName + "_Controller.php", 'w')

    controller.write('<?php' + EOL)
    controller.write(EOL)
    controller.write('include __DIR__.\'/../Functions/gatherData.php\';' + EOL)
    controller.write(EOL)
    controller.write(EOL)
    controller.write('if(!$_GET){' + EOL)
    controller.write(ST + '//Fill' + EOL)
    controller.write('}' + EOL)
    controller.write(EOL)
    controller.write('else{' + EOL)
    controller.write(EOL)
    controller.write(ST + 'switch($_GET[\'action\']){' + EOL)
    controller.write(EOL)
    for action in actionList:
        controller.write(DT + 'case \'' + action + '\':' + EOL)
        controller.write(DT + 'if(!$_POST){' + EOL)
        controller.write(TT + '//Fill' + EOL)
        controller.write(DT + '} else {' + EOL)
        controller.write(TT + '//Fill' + EOL)
        controller.write(DT + '}' + EOL)
        controller.write(DT + 'break;' + EOL)
        controller.write(EOL)
    controller.write(ST + '}' + EOL)
    controller.write('}' + EOL)
    controller.write(EOL)
    controller.write('?>' + EOL)

    controller.close()

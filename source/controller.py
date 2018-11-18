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

    controller.write('<?php\r\n')
    controller.write('\r\n')
    controller.write('include __DIR__.\'/../Functions/gatherData.php\';\r\n')
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

def createGatherData(absolute_output_path):
    '''
    Gather Data initial unfilled script creation
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    gather = open(absolute_output_path + '/Functions/gatherData.php', 'w')

    gather.write('<?php\r\n')
    gather.write('\r\n')
    gather.write('//Fill with includes\r\n')
    gather.write('\r\n')

    gather.close()

def appendToGatherData(entityName, attributesList, absolute_output_path):
    '''
    Append to gatherData.php file
    @Param entityName: Name of the entity.
    @Param attributesList: List of all attributes of the entity.
    @Param absolute_output_path: Path where the hole output is going to be written
    '''
    originalName = entityName
    originalName = originalName.lower()
    originalName = originalName.title()
    originalName = originalName.replace(" ", "_")
    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "")

    gather = open(absolute_output_path + '/Functions/gatherData.php', 'a+')

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

def closeGatherData(absolute_output_path):
    '''
    Close PHP Tag on gatherData.php
    @Param absolute_output_path: Path where the hole output is going to be written
    '''
    gather = open(absolute_output_path + '/Functions/gatherData.php', 'a+')

    gather.write('?>')

    gather.close()
